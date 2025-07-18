from typing import List

class Solution:
    @staticmethod
    def two_sum1(nums: List[int], target: int) -> List[int]:
        """
        求解两数之和
        :param nums:
        :param target:
        :return:
        """
        for index1, i in enumerate(nums):
            for index2, j in enumerate(nums):
                if index1 != index2 and i + j == target:
                    return [index1, index2]
        return []

    @staticmethod
    def two_sum2(nums: List[int], target: int) -> List[int]:
        for index1, i in enumerate(nums):
            index2 = nums.index(target - i)
            if target-i in nums[index1+1:] and index1 != index2:
                return [index1, index2]
        return []

    @staticmethod
    def two_sum3(nums: List[int], target:int) -> List[int]:
        hash_table: dict = {}
        for index1, i in enumerate(nums):
            try:
                index2 = hash_table[target-i]
                return [index2, index1]
            except KeyError:
                pass
            hash_table[i] = index1
        return []


if __name__ == '__main__':
    Solution.two_sum1([2, 9, 11, 15], 17)
    Solution.two_sum2([2, 9, 11, 15], 17)
    print(Solution.two_sum3([2, 9, 11, 15], 13))