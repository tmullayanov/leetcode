from typing import *


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
        for _ in range(k):
            self.rotateRightByOne(nums)

    def rotateRightByOne(self, nums: List[int]) -> None:
        n = len(nums)
        last = cur = nums[0]
        for i in range(n):
            cur = nums[i]
            nums[i] = last
            last = cur
        nums[0] = cur


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    Solution().rotate(nums, k)
    print(f'{nums=}')
    print('aaaa')
