"""
基本思想:
从牌堆的牌顶拿出一张牌, 插入手牌中
插入条件是, 如果牌大于手牌的尾牌将其插入手牌末尾, 如果小于尾牌, 判断其是否大于手牌尾牌的前一张, 如果不成立继续判断,直到手牌的首牌为止


"""


def insertion_sort(array):
    """
    伪代码:
    :param array:
    :return:
    """

    # We start from 1 since the first element is trivially sorted
    for index in range(1, len(array)):
        # 取得其中第二个元素
        current_value = array[index]
        # 创建一个指针
        current_position = index
        # print(f'index: {index}, value: {current_value}), current_position: {current_position}')
        # As long as we haven't reached the beginning and there is an element
        # in our sorted array larger than the one we're trying to insert - move
        # that element to the right
        # 只要我们还没循环到起始处, 只要将要插入的元素大于排序的数组, 就将这个元素移动到右边
        print('A', current_value, current_position, array)
        while current_position > 0 and array[current_position - 1] > current_value:

            # 如果被比较的值大于当前值, 将其插入到当前位置
            array[current_position] = array[current_position - 1]
            # print(f"当前要插入的值{current_value}, 左边的值:{array[current_position - 1]}> 当前值{current_value}, 修改当前位置的值"
            #       f"为{array[current_position-1]}")
            print('B', current_value, current_position, array)
            current_position = current_position - 1

        # We have either reached the beginning of the array or we have found
        # an element of the sorted array that is smaller than the element
        # we're trying to insert at index current_position - 1.
        # Either way - we insert the element at current_position
        array[current_position] = current_value
        print('C', current_value, current_position, array)
        print(f'---{index}---')


if __name__ == '__main__':
    my_array = [4, 22, 41, 40, 27, 30, 36, 16, 42, 37, 14, 39, 3, 6, 34, 9, 21, 2, 29, 47]
    print(my_array)
    insertion_sort(my_array)
    print(my_array)
