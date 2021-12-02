from typing import *


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        symbols = {}
        for char in s:
            symbols[char] = symbols.get(char, 0) + 1
        for char in t:
            if char not in symbols:
                return False
            symbols[char] -= 1
        return all(x == 0 for x in symbols.values())


if __name__ == '__main__':
    tests = (
        ("😂123", "1😂32", True),
        ("abc", "cba", True),
        ('abc', 'd', False),
        ('avc', '123', False)
    )
    for (s1, s2, expected) in tests:
        print(f'ans={Solution().isAnagram(s1, s2)} {expected=}')
