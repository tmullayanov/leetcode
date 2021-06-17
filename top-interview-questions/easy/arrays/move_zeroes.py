from typing import *


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write_idx = -1
        for (read_idx, elem) in enumerate(nums):
            if elem != 0:
                write_idx += 1
                nums[read_idx], nums[write_idx] = nums[write_idx], nums[read_idx]
        return


if __name__ == '__main__':
    tests = (
        [0, 1, 0, 3, 12],
        [0]
    )

    for test in tests:
        print(f'{test=}', end=' ')
        Solution().moveZeroes(test)
        print(f'answer={test}')
