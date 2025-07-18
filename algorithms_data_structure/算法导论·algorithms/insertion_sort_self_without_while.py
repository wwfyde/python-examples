"""
基本思想:
从牌堆的牌顶拿出一张牌, 插入手牌中
插入条件是, 如果牌大于手牌的尾牌将其插入手牌末尾, 如果小于尾牌, 判断其是否大于手牌尾牌的前一张, 如果不成立继续判断,直到手牌的首牌为止


"""


def insertion_sort(array):

    # We start from 1 since the first element is trivially sorted
    new_array = [array[0]]
    for index, value in enumerate(array[1:]):

        # 重复新数组的长度的次数
        print(index, value)
        for current_position in reversed(range(len(new_array))):
            if value >= new_array[current_position]:
                print(f"第{index+1}次插入, 将{value}插入数组{new_array}中的第{current_position+1}位")
                new_array.insert(current_position+1, value)
                break

            if current_position == 0:
                print(f"第{index+1}次插入, 将{value}插入数组{new_array}中的第{current_position}位")
                new_array.insert(0, value)
                pass
    return new_array


if __name__ == '__main__':
    # my_array = [4, 22, 41, 40, 40, 27, 30, 36, 16, 42, 37, 14, 39, 3, 6, 34, 9, 21, 2, 29, 47]
    my_array = [5, 2, 4, 6, 1, 3]
    print("array:", my_array, len(my_array))
    my_new_array = insertion_sort(my_array)
    print("sorted array: ", my_new_array, len(my_new_array))
