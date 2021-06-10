from typing import *


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        # otherwise we have to do some real work
        first, second, third = float('-inf'), float('-inf'), float('-inf')

        for elem in nums:
            if elem > first:
                first = elem

        for elem in nums:
            if elem > second and elem < first:
                second = elem

        for elem in nums:
            if elem > third and elem < second:
                third = elem

        if third == float('-inf'):
            return first

        return third


if __name__ == '__main__':
    tests = (
        [3, 2, 1],
        [1, 2],
        [1],
        [2, 2, 3, 1],
        [1, 3, 3, 3, 2, 5],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1, 3, 2, 6, 5, 4, 7],
        [1, 1, 2]
    )
    # tests = (
    #     [1, 2, 3, 4, 5],
    # )

    for test in tests:
        print(f'{test=} answer={Solution().thirdMax(test)}')
