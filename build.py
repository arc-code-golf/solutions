import sys
from pathlib import Path

import compress

input_dir = Path("solutions")
output_dir = Path("build")


def main() -> None:
    if len(sys.argv) > 1:
        task_num = int(sys.argv[1])
        tasks: list[int] = [task_num]
    else:
        tasks = range(1, 401)

    assert input_dir.exists(), f"{input_dir} does not exist"
    output_dir.mkdir(exist_ok=True)

    for i in tasks:
        filename = f"task{i:03d}.py"
        with (input_dir / filename).open(encoding="latin-1") as f:
            content = f.read()

        source_content = content.split("\n#")[0]
        source_bytes = source_content.encode("latin-1")

        directives: dict[str, str] = {}
        for line in content.split("\n"):
            if line.startswith("# ") and ":" in line:
                key, _, value = line[2:].partition(":")
                directives[key.strip()] = value.strip()

        compression = directives.get("compression")

        if compression == "frozen":
            huffman_hex = directives.get("huffman", "")
            if not huffman_hex:
                print(f"Warning: {filename} has frozen compression but no huffman")
                output = source_bytes
            else:
                output = compress.compress_frozen(source_bytes, huffman_hex)
            with (output_dir / filename).open("wb") as f:
                f.write(output)

        elif compression == "auto":
            compressed, _ = compress.compress(source_bytes)
            with (output_dir / filename).open("wb") as f:
                f.write(compressed)

        else:
            with (output_dir / filename).open("w", encoding="latin-1") as f:
                f.write(source_content)


if __name__ == "__main__":
    main()
