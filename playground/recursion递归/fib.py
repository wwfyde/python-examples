"""
斐波那契额数列
fib(n) = fib(n-1) + fib(n-2)
fib(0) = 0
fib(1) = 1
"""

import time


def fib(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    print(fib(1))
    print(fib(2))
    print(fib(3))
    print(fib(4))
    print(fib(5))
    print(fib(6))
    print(fib(10))
    assert fib(5) == 5
    assert fib(6) == 8
    # 1, 1, 2, 3, 5, 8
    start = time.time()
    fib_list = [fib(i) for i in range(40)]  # 需要19.64秒
    end = time.time()
    print(end - start)
    print(fib_list)
    fib = fib_generator()
    start = time.time()
    fib_list2 = [next(fib) for _ in range(40)]  # 只需要2.59秒
    end = time.time() - start
    print(end)
