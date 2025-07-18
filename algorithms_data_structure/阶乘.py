
# 求解值n的阶乘
def 阶乘(n: int) -> int:
    """
    求解n!的值
    :param n: 非零自然数
    :return:
    """
    result = 1
    if isinstance(n, int) and n >= 1:

        for i in range(1, n+1):
            result *= i
        return result
    else:
        return -1


if __name__ == '__main__':
    print(阶乘(10))
