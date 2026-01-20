import zlib
from dataclasses import dataclass

import deflate
import zopfli.zlib

from reencode import Huffman, lz77, reencode


@dataclass(frozen=True)
class CompressionInfo:
    method: str
    window: int
    delimiter: str
    reencode: bool


ZOPFLI_ITERS: list[int] = [15, 128]
LIBDEFLATE_LEVELS: list[int] = [11, 12]
ZLIB_LEVELS: list[int] = [9]
DELIMS: list[bytes] = [b"'", b'"']
WINDOWS: list[int] = [-9, -10]


def _hoist_import(src: bytes) -> tuple[bytes, bytes]:
    if src.startswith(b"import"):
        module = src.split()[1]
        return src[len(module) + 8 :], b"," + module
    return src, b""


def _sanitize(b_in: bytes, delim: bytes) -> bytes:
    b_out = bytearray()
    for b, b_next in zip(b_in, [*b_in[1:], 0]):
        if b == 0:
            b_out += b"\\x00" if b_next in b"01234567" else b"\\0"
        elif b == ord("\r"):
            b_out += b"\\r"
        elif b == ord("\\") and b_next in b"\0\n\r\"'01234567NU\\abfnrtuvx":
            b_out += b"\\\\"
        elif b == ord("\n") and len(delim) == 1:
            b_out += b"\\n"
        elif bytes([b]) == delim:
            b_out += b"\\" + delim
        else:
            b_out.append(b)
    return bytes(b_out)


def _wrap(deflate_data: bytes, delim: bytes, hoisted: bytes, window: int) -> bytes:
    sanitized = _sanitize(reencode(deflate_data, delim), delim)
    window_str = b",~9" if window == -10 else (b",%d" % window if window != 15 else b"")
    return (
        b"#coding:L1\nimport zlib"
        + hoisted
        + b"\nexec(zlib.decompress(bytes("
        + delim
        + sanitized
        + delim
        + b',"L1")'
        + window_str
        + b"))"
    )


def compress(src: bytes) -> tuple[bytes, CompressionInfo]:
    src, hoisted = _hoist_import(src)
    compressed_data: list[tuple[bytes, str, int]] = []

    for iters in ZOPFLI_ITERS:
        full: bytes = zopfli.zlib.compress(
            src,
            numiterations=iters,
            blocksplitting=False,
        )
        result = full[2:-4]
        actual_window = -(((full[0] >> 4) & 0x0F) + 8)
        compressed_data.append((result, f"zopfli(iters={iters})", -10))
        if actual_window != -10:
            compressed_data.append(
                (
                    result,
                    f"zopfli(iters={iters})",
                    -9 if actual_window < 15 else actual_window,
                ),
            )

    compressed_data.extend(
        (
            bytes(deflate.deflate_compress(src, compresslevel=level)),
            f"libdeflate(level={level})",
            -10,
        )
        for level in LIBDEFLATE_LEVELS
    )

    for level in ZLIB_LEVELS:
        for window in WINDOWS:
            result = zlib.compress(
                src,
                level=level,
                wbits=-15 if window == -10 else window,
            )
            compressed_data.append((result, f"zlib(level={level})", window))

    candidates: list[tuple[bytes, CompressionInfo]] = []
    for data, method, window in compressed_data:
        for delim in DELIMS:
            for use_reencode in [True, False]:
                sanitized = _sanitize(
                    reencode(data, delim) if use_reencode else data,
                    delim,
                )
                window_str = (
                    b",~9"
                    if window == -10
                    else (b",%d" % window if window != 15 else b"")
                )
                code = (
                    b"#coding:L1\nimport zlib"
                    + hoisted
                    + b"\nexec(zlib.decompress(bytes("
                    + delim
                    + sanitized
                    + delim
                    + b',"L1")'
                    + window_str
                    + b"))"
                )
                candidates.append(
                    (
                        code,
                        CompressionInfo(
                            method=method,
                            window=window,
                            delimiter=delim.decode(),
                            reencode=use_reencode,
                        ),
                    ),
                )

    return min(candidates, key=lambda x: len(x[0]))


def compress_frozen(src: bytes, huffman_hex: str) -> bytes:
    src, hoisted = _hoist_import(src)
    huffman = Huffman.parse(bytes.fromhex(huffman_hex))
    candidates = [_wrap(lz77(src, huffman, d), d, hoisted, -10) for d in DELIMS]
    return min(candidates, key=len)
