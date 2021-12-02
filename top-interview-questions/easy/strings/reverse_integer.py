from typing import *

'''
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1],
then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
'''


class Solution:
    MAX_INT = 2**31 - 1
    MIN_INT = - 2**31
    LAST_DIGIT_MAX = MAX_INT % 10
    LAST_DIGIT_MIN = MIN_INT % 10

    def reverse(self, x: int) -> int:
        pop = 0
        tmp = 0
        rev = 0

        while x:
            pop = x % 10
            if x > 0:
                rev_overflow = rev > (Solution.MAX_INT // 10)
                rev_pop_overflow = rev == (
                    Solution.MAX_INT // 10) and pop > Solution.LAST_DIGIT_MAX
                if rev_overflow or rev_pop_overflow:
                    return 0
            elif x < 0:
                pop = 0 if pop == 0 else pop - 10  # python keeps % positive.
                rev_overflow = rev < int(Solution.MIN_INT / 10)
                rev_pop_overflow = rev == int(
                    Solution.MIN_INT / 10) and pop < Solution.LAST_DIGIT_MIN
                if rev_overflow or rev_pop_overflow:
                    return 0

            x = int(x/10)
            tmp = rev * 10 + pop
            rev = tmp

        return rev


if __name__ == '__main__':
    print(Solution().reverse(134))
    print(Solution().reverse(-134))
    print(Solution().reverse(2**31-9))
    print(Solution().reverse(-(2**31-9)))
    print(Solution().reverse(10))
    print(Solution().reverse(-10))
