import math


def triangle_area(a: int, b: int, c: int) -> float:
    area = 0
    if all([a > 0, b > 0, c > 0]):
        p = (a + b + c) / 2

        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    else:
        area = -1

    return area


if __name__ == '__main__':
    print(f"{triangle_area(6, 8, 12):0.8}")
