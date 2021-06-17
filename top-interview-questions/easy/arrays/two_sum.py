from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for (idx, n) in enumerate(nums):
            if n in complements:
                return [complements[n], idx]
            else:
                complements[target - n] = idx


if __name__ == '__main__':
    tests = (
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
        ([3, 2, 1, 3], 6)
    )

    for test in tests:
        nums, target = test
        print(f'{test=} answer={Solution().twoSum(nums, target)}')
