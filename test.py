import copy
import sys
import warnings
from argparse import ArgumentParser
from multiprocessing import Pool, cpu_count
from pathlib import Path

import numpy as np

from common import Task, load_solution

TASKS = Path("tasks")


def test_task(args: tuple[int, Path, int | None]) -> tuple[int, bool, int]:
    task_num, solutions_dir, max_cases = args

    task = Task.load(task_num, TASKS)
    module = load_solution(task_num, solutions_dir)
    p = getattr(module, "p")

    path = solutions_dir / f"task{task_num:03d}.py"

    testcases = task.all_testcases()
    if max_cases is not None:
        testcases = testcases[:max_cases]

    passed = total = 0
    for testcase in testcases:
        total += 1
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                input_copy = copy.deepcopy(testcase.input)
                output = p(input_copy)
                if np.array_equal(np.array(output), np.array(testcase.output)):
                    passed += 1
        except Exception:
            pass

    return task_num, passed == total, path.stat().st_size


def main() -> None:
    parser = ArgumentParser(description="Test solutions")
    parser.add_argument(
        "tasks",
        nargs="*",
        type=int,
        help="Task numbers (default: all)",
    )
    parser.add_argument(
        "-j",
        "--jobs",
        type=int,
        default=cpu_count(),
        help="Worker count",
    )
    parser.add_argument(
        "-d",
        "--directory",
        type=str,
        default="build",
        help="Solutions directory (default: build)",
    )
    parser.add_argument(
        "-n",
        "--max-cases",
        type=int,
        default=None,
        help="Maximum test cases per task (default: all)",
    )
    args = parser.parse_args()

    tasks: list[int] = args.tasks or [*range(1, 401)]
    jobs: int = args.jobs
    solutions_dir = Path(args.directory)
    max_cases: int | None = args.max_cases

    tasks_list = [(task_num, solutions_dir, max_cases) for task_num in tasks]
    with Pool(jobs) as pool:
        results = [r for r in pool.imap_unordered(test_task, tasks_list) if r]

    results.sort()

    ok_count = sum(ok for _, ok, _ in results)
    total_score = sum(max(1, 2500 - bytes_count) for _, _, bytes_count in results)
    failed = [task_num for task_num, ok, _ in results if not ok]

    print(f"Passed: {ok_count}/{len(results)}")
    print(f"Score: {total_score}")

    if failed:
        print(f"Failed tasks: {failed}")
        sys.exit(1)


if __name__ == "__main__":
    main()
