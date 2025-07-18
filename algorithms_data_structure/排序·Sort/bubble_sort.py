# 冒泡排序
from typing import MutableSequence


def bubble_sort(array: MutableSequence) -> MutableSequence:
    """
    从最后array[n-1]和array[n-2]开始,若array[n-1]<array[n-2]则相互交换值, 依次递减, 直到比较a[1]和a[0];
    array[0]排序完成, 依次排序array[1]...array[n-1] 最终完成排序

    :param array:
    :return:
    """
    n = len(array)
    for j in range(1, n):  # 第一轮找出最小的, 找出第二小的
        for i in range(n-1, j-1, -1):
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]

    return array


if __name__ == '__main__':
    res = bubble_sort([71, 2, 5, 3, 1, 19])
    print(res)



