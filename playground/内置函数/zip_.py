from typing import List

type Matrix = List[List[int]]


def transpose_matrix(matrix: Matrix) -> Matrix:
    """

    :type matrix: object
    """
    return list(map(list, zip(*matrix)))


if __name__ == '__main__':

    matrix_ = [
        [1, 2, 3],
        [4, 5, 6],
        # [7, 8, 9]
    ]

    transpose_matrix = list(map(list, zip(*matrix_)))

    for row in transpose_matrix:
        print(row)
