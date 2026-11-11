from typing import List


class Solution:

    @staticmethod
    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:m+n] = nums2[:n]
        nums1 = nums1[:m+n]
        nums1.sort()
        print(nums1)


if __name__ == '__main__':
    s = Solution()
    s.merge([1, 2, 3, 0, 0, 0, 4, 5], 3, [2, 5, 6], 3)
