"""
基本思想:
从牌堆的牌顶拿出一张牌, 插入手牌中, 手牌是恒定排序好的数组
插入条件是, 当
将问题转换为数学
可以将所有牌看成一个整体 然后分成两堆, 三部分. 特殊的是被拿起的那张牌, 每次循环时应该保证这三个部分是正确的
"""


def insertion_sort(array: list):
    for j in range(1, len(array)):
        # 关键字 手牌 被比较的牌
        key = array[j]
        # 循环不变式 a[0]
        immutable_array = [array[0]]
        
        # 需要与循环不变式比较的次数, 循环不变式的长度
        # 每次迭代循环不变式 i指向循环不等式的长度, 初始长度为1
        i = j
        
        # 当循环不变式中的值大于关键字时,
        # print('outer', i, array[i-1], key)
        # 直到i<=0 或左边的值小于等于key 停止
        # print(array)
        while i > 0 and array[i-1] > key:
            # 将大于关键字的元素移到右边

            # print('移位前', array[i], array[i-1])
            # 将左侧的数移位到右边
            array[i] = array[i-1]
            # 迭代到 i = 0结束
            i = i - 1
            # print(i, array[i-1], key)

        
        # 将关键字加到循环不变式中的末尾中
        # print(i)
        # print('-')
        # print(array)
        # 将key 插入到数组中
        array[i] = key
        print('循环不变式:', array[:j+1])
        # print(array)


if __name__ == '__main__':
    # my_array = [4, 22, 41, 40, 27, 30, 36, 16, 42, 37, 14, 39, 3, 6, 34, 9, 21, 2, 29, 47]
    array = [5, 2, 4, 6, 1, 3]
    print("array:", array, len(array))
    insertion_sort(array)
    print("sorted array use built-in function: ", sorted(array), len(sorted(array)))
    print("sorted array: ", array, len(array))
