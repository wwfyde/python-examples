"""
斐波那契额数列
fib(n) = fib(n-1) + fib(n-2)
fib(0) = 0
fib(1) = 1
"""


def fib(n: int):

    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    print(fib(1))
    print(fib(2))
    print(fib(3))
    print(fib(4))
    print(fib(5))
    print(fib(6))
    assert fib(5) == 5
    assert fib(6) == 8
    # 1, 1, 2, 3, 5, 8
