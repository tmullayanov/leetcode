from typing import *


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        read_idx, write_idx = 0, 0
        n = len(nums)
        while read_idx < n:
            if nums[read_idx] != 0:
                nums[read_idx], nums[write_idx] = nums[write_idx], nums[read_idx]
                write_idx += 1
            read_idx += 1
