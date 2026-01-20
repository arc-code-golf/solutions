import sys
from argparse import ArgumentParser

from blessed import Terminal

from common import Task, TestCase


def print_matrix(term: Terminal, matrix: list[list[int]]) -> None:
    colours = {
        0: term.on_gray20,
        1: term.on_blue,
        2: term.on_red,
        3: term.on_green,
        4: term.on_yellow,
        5: term.on_gray50,
        6: term.on_magenta,
        7: term.on_orange3,
        8: term.on_cyan,
        9: term.on_maroon,
    }

    for row in matrix:
        for val in row:
            num = f"{val:2}" if val != 0 else "  "
            color = colours.get(val, term.on_white)
            print(color(num), end="")
        print()


def show_testcase(
    term: Terminal,
    testcase: TestCase,
    label: str,
    task_num: int,
    tc_idx: int,
    total_tcs: int,
    *,
    interactive: bool = True,
) -> None:
    print(term.home + term.clear, end="")
    if interactive:
        print("h/l: task, j/k: testcase, g: jump testcase, t: jump task, q: quit")
    print()
    print(
        term.bold_underline(f"Task {task_num:03d}")
        + f" - {label} ({tc_idx + 1}/{total_tcs})",
    )
    print()
    print(f"Input ({len(testcase.input)}x{len(testcase.input[0])}):")
    print()
    print_matrix(term, testcase.input)
    print()
    print(f"Output ({len(testcase.output)}x{len(testcase.output[0])}):")
    print()
    print_matrix(term, testcase.output)
    print()


def main() -> None:
    parser = ArgumentParser(description="Show ARC tasks")
    parser.add_argument("task", nargs="?", type=int, default=1, help="Task number")
    parser.add_argument(
        "testcase",
        nargs="?",
        type=int,
        default=1,
        help="Test case number",
    )
    parser.add_argument("-p", "--print", action="store_true", help="Print and quit")
    args = parser.parse_args()

    task_num = args.task
    tc_idx = args.testcase - 1
    term = Terminal()

    if args.print:
        task = Task.load(task_num)
        examples = task.all()
        if tc_idx >= len(examples):
            print(f"Test case {tc_idx + 1} does not exist")
            sys.exit(1)
        label, testcase = examples[tc_idx]
        show_testcase(
            term,
            testcase,
            label,
            task_num,
            tc_idx,
            len(examples),
            interactive=False,
        )
        return

    try:
        with term.cbreak(), term.hidden_cursor(), term.fullscreen():
            task = Task.load(task_num)
            examples = task.all()

            while True:
                label, testcase = examples[tc_idx]
                show_testcase(term, testcase, label, task_num, tc_idx, len(examples))

                key = term.inkey()

                if key == "h" or key.name == "KEY_LEFT":
                    task_num = max(1, task_num - 1)
                    task = Task.load(task_num)
                    examples = task.all()
                    tc_idx = 0
                elif key == "l" or key.name == "KEY_RIGHT":
                    task_num = min(400, task_num + 1)
                    task = Task.load(task_num)
                    examples = task.all()
                    tc_idx = 0
                elif key == "k" or key.name == "KEY_UP":
                    tc_idx = (tc_idx - 1) % len(examples)
                elif key == "j" or key.name == "KEY_DOWN":
                    tc_idx = (tc_idx + 1) % len(examples)
                elif key == "g":
                    print(term.move_y(term.height - 1) + "Jump to testcase: ", end="")
                    sys.stdout.flush()
                    num_str = ""
                    while True:
                        k = term.inkey()
                        if k.name == "KEY_ENTER":
                            if num_str:
                                new_tc = int(num_str) - 1
                                if 0 <= new_tc < len(examples):
                                    tc_idx = new_tc
                            break
                        if k.name == "KEY_ESCAPE":
                            break
                        if k.isdigit():
                            num_str += k
                            print(k, end="")
                            sys.stdout.flush()
                        elif k.name == "KEY_BACKSPACE" and num_str:
                            num_str = num_str[:-1]
                            print("\b \b", end="")
                            sys.stdout.flush()
                elif key == "t":
                    print(term.move_y(term.height - 1) + "Jump to task: ", end="")
                    sys.stdout.flush()
                    num_str = ""
                    while True:
                        k = term.inkey()
                        if k.name == "KEY_ENTER":
                            if num_str:
                                new_task = int(num_str)
                                if 1 <= new_task <= 400:
                                    task_num = new_task
                                    task = Task.load(task_num)
                                    examples = task.all()
                                    tc_idx = 0
                            break
                        if k.name == "KEY_ESCAPE":
                            break
                        if k.isdigit():
                            num_str += k
                            print(k, end="")
                            sys.stdout.flush()
                        elif k.name == "KEY_BACKSPACE" and num_str:
                            num_str = num_str[:-1]
                            print("\b \b", end="")
                            sys.stdout.flush()
                elif key == "q":
                    break
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
