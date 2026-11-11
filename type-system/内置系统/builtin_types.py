from typing import Callable


def run(f: Callable[[int], int], items: list) -> list:
    a = map(f, items)
    return list(a)


if __name__ == "__main__":

    def m(x: int):
        return x**2

    result = run(m, [1, 2, 3])
    print(result)
