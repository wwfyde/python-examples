from typing import List


# partition_strings
# 基本思路是, 按索引取元素,
def partition_string(s: str, step: int) -> List:
    """ Partition string to chunks
    :param s: the string that you want to partition
    :param step: chunks size you want to have
    :return: chunk list of partitioned elements
    """
    return [s[i:i + step] for i in range(0, len(s), step)]


if __name__ == '__main__':
    print(partition_string("wwfyde", 7))
    assert partition_string("wwfyde", 1) == ['w', 'w', 'f', 'y', 'd', 'e']
