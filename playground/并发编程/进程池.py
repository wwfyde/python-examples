"""
进程池编程思路

"""

import concurrent.futures
import math

# 任务列表: 质数
PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]


# 任务实现
def is_prime(n):

    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))

    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    # 实例化进程池
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # 根据任务数量创建进程
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print(f"{number} is prime: {prime}")


if __name__ == '__main__':
    main()
    import 装饰器.类装饰器

    print(装饰器.类装饰器.__name__)