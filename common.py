import importlib.util
import json
import warnings
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types import ModuleType


@dataclass(frozen=True, slots=True)
class TestCase:
    input: list[list[int]]
    output: list[list[int]]

    @staticmethod
    def from_dict(data: dict) -> "TestCase":
        return TestCase(data["input"], data["output"])


@dataclass(frozen=True, slots=True)
class Task:
    train: list[TestCase]
    test: list[TestCase]
    arc_gen: list[TestCase]

    def all(self) -> list[tuple[str, TestCase]]:
        examples = []
        for i, testcase in enumerate(self.train):
            examples.append((f"Train {i + 1}", testcase))
        for i, testcase in enumerate(self.test):
            examples.append((f"Test {i + 1}", testcase))
        for i, testcase in enumerate(self.arc_gen):
            examples.append((f"ARC-Gen {i + 1}", testcase))
        return examples

    def all_testcases(self) -> list[TestCase]:
        return self.train + self.test + self.arc_gen

    @staticmethod
    def from_dict(data: dict) -> "Task":
        train = [TestCase.from_dict(tc) for tc in data["train"]]
        test = [TestCase.from_dict(tc) for tc in data["test"]]
        arc_gen = [TestCase.from_dict(tc) for tc in data["arc-gen"]]
        return Task(train, test, arc_gen)

    @staticmethod
    def load(task_num: int, tasks_dir: Path = Path("tasks")) -> "Task":
        task_filename = f"task{task_num:03d}.json"
        task_path = tasks_dir / task_filename
        with task_path.open() as f:
            task_data = json.load(f)
        return Task.from_dict(task_data)


def load_solution(task_num: int, solutions_dir: Path = Path("merged")) -> ModuleType:
    path = solutions_dir / f"task{task_num:03d}.py"
    if not path.exists():
        raise FileNotFoundError(f"Solution file not found: {path}")

    spec = importlib.util.spec_from_file_location("solution", path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load spec from {path}")

    module = importlib.util.module_from_spec(spec)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        spec.loader.exec_module(module)

    return module
