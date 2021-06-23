from typing import *


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = {}
        for n in nums:
            if n in h:
                return True
            else:
                h[n] = True
        return False


if __name__ == '__main__':
    tests = (
        [1, 1, 2],
        [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
        [1, 2, 3],
        [1]
    )

    for test in tests:
        print(f'{test=} answer={Solution().containsDuplicate(test)}')
