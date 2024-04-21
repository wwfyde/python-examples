from typing import overload


@overload
def add(a: int, b: int) -> int:
    return a + 2 * b


@overload
def add(a: float, b: float) -> float:
    return a + 2 * b


def add(a: int | float, b: int | float) -> int | float:
    return a + 2 * b


print(add(12.3, 12.7))
