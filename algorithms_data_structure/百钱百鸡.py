# 已知 a+b+c=100; 5a+3b+c/3=100; c%3=0
from typing import Tuple, List

N = 100


def 百钱百鸡() -> List[Tuple[int, int, int]]:
    l: List[Tuple[int, int, int]] = []
    for c in range(0, N + 1, 3):
        for b in range(0, N - c):
            for a in range(0, N-c-b):
                if c % 3+3 * b + a * 5 == N:
                    l.append((a, b, c))
    return l


if __name__ == '__main__':
    print(百钱百鸡())
