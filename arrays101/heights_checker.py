from typing import *


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        return sum(1 for (lhs, rhs) in
                   zip(heights, expected) if lhs != rhs)


class SolutionFast:
    def heightChecker(self, heights):
        expected = sorted(heights)
        s = 0
        l = len(heights)
        for i in range(l):
            if heights[i] != expected[i]:
                s += 1
        return s


if __name__ == '__main__':
    tests = (
        ([5, 1, 2, 3, 4], 5),
        ([1, 2, 3, 4, 5], 0),
        ([], 0),
        ([1, 1, 4, 2, 1, 3], 3)
    )

    for (test, exp) in tests:
        print('OK' if Solution().heightChecker(test) == exp else 'FAIL')
    print('----------')
    for (test, exp) in tests:
        print('OK' if SolutionFast().heightChecker(test) == exp else 'FAIL')
