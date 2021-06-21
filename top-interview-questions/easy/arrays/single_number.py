from typing import *


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from functools import reduce
        return reduce(lambda acc, curr: acc ^ curr, nums)


if __name__ == '__main__':
    tests = (
        ([1, 1, 2, 2, 3], 3),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1)
    )

    for (nums, answer) in tests:
        print(f'{nums=} {answer=} solution={Solution().singleNumber(nums)}')
