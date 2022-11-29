import timeit
from pathlib import Path
from typing import Callable


INPUT_FP = Path(__file__).parent / "input.txt"


def read_input(fp: Path) -> list[int]:
    with open(fp, "r") as f:
        data = list(map(int, f.read().splitlines()))
    return data


def print_solution(val: str, time: float | None = None) -> None:
    print(f"\nSolution:\t{val}")
    if time is not None:
        print(f"Duration:\t{time:.6f}s")


def execute(func: Callable, *args) -> tuple[int, float]:
    t = timeit.Timer(lambda: func(*args))
    t_avg = t.timeit(10_000) / 10_000
    return func(*args), t_avg


def calc(data: list[int]) -> int:
    prev = data[0]
    inc = 0
    for e in data[1:]:
        if e > prev:
            inc += 1
        prev = e
    return inc


def main() -> None:
    data = read_input(INPUT_FP)

    val, t_avg = execute(calc, data)

    print_solution(val, t_avg)


if __name__ == "__main__":
    main()
