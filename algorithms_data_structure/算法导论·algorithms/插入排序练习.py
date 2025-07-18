def insertion_sort(array: list, sorted_array: list = []) -> list:

    sorted_array.insert(array[0])

    for index, item in enumerate(array[1:]):

        print(index, item)

        # 已排序好数组长度
        key = item
        for sorted_item in range(index):
            if item > sorted_array[-1]:

                # 什么时候插入, 如果牌比手牌中的左边一张大则插入
                sorted_array.insert(item)
                break


    return array


if __name__ == '__main__':
    # my_array = [4, 22, 41, 40, 27, 30, 36, 16, 42, 37, 14, 39, 3, 6, 34, 9, 21, 2, 29, 47]
    my_array = [5, 2, 4, 6, 1, 3]
    insertion_sort(my_array)