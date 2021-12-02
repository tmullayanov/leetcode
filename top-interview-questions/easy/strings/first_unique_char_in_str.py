from typing import *


class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        unique = []

        for c in s:
            if c not in seen:
                seen.add(c)
                unique.append(c)
            else:
                if c in unique:
                    unique.remove(c)
        if unique:
            return s.index(unique[0])
        return -1


if __name__ == '__main__':
    tests = (
        ('leetcode', 0),
        ('aabb', -1),
        ('aba', 1)
    )

    for (test, expected) in tests:
        print(f'{test=} ans={Solution().firstUniqChar(test)} {expected=}')
