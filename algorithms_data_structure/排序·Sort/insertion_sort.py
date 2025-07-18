# 插入排序
from typing import List


def insert_sort(arr: List[int]) -> List[int]:
    """
    将列表分类两个部分已排序arr[:i]和未排序arr[i:]
    config未排序分组中取下首位并存储
    将arr[i]插入arr[:i], >=则不动, 小于则插入
    :param arr:
    :return:
    """
    for i in range(1, len(arr)):  # 移动i指针以排序
        print(type(repr(i)))
        r = arr[i]  # 记录操作的数
        j = i - 1  # 创建j指针
        while j >= 0 and r < arr[j]:  # 当r>=arr[j]或j<0时停止
            arr[j + 1] = arr[j]  # 将记录后裔
            j -= 1  # 移动指针
        arr[j + 1] = r  # 将操作对象插入正确位置

    return arr  # 可以不用返回, 因为,该算法是直接修改的传入的列表


if __name__ == '__main__':
    arr1 = [2, 1]
    insert_sort(arr1)
    print(arr1)
