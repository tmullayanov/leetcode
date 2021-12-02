from typing import *


class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum_syms = ''.join(filter(str.isalnum, s)).lower()
        l = len(alnum_syms)
        for i in range(l//2):
            if alnum_syms[i] != alnum_syms[l - 1 - i]:
                return False

        return True


if __name__ == '__main__':
    tests = (
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False)
    )

    for (test, expected) in tests:
        print(f'{test=} ans={Solution().isPalindrome(test)} {expected=}')
