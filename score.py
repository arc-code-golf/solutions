import sys
from pathlib import Path


def calculate_score(directory: Path) -> int:
    total_score = 0

    for problem in range(1, 401):
        problem_file = directory / f"task{problem:03d}.py"
        if problem_file.exists():
            bytes_count = problem_file.stat().st_size
            score = max(1, 2500 - bytes_count)
            total_score += score

    return total_score


if __name__ == "__main__":
    print(calculate_score(Path(sys.argv[1])))
