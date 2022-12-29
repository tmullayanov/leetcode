from typing import *


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        previous = self.countAndSay(n - 1)
        say = (str(count) + sym for (sym, count) in self.group(previous))
        return ''.join(say)

    def group(self, s: str) -> Generator[Tuple[str, int], None, None]:
        if not s:
            return
        cur_sym, cur_count = s[0], 1
        for sym in s[1:]:
            if cur_sym != sym:
                yield (cur_sym, cur_count)
                cur_sym = sym
                cur_count = 1
            else:
                cur_count += 1
        yield (cur_sym, cur_count)


if __name__ == '__main__':
    tests = (
        (1,     1),
        (2,     11),
        (3,     21),
        (4,     1211),
        (5,     111221),
        (6,     312211),
        (7,     13112221),
        (8,     1113213211),
        (9,     31131211131221),
        (10,    13211311123113112211),
    )
    for (n, ans) in tests:
        actual = Solution().countAndSay(n)
        print(
            f'{n=:<5} | {ans=:<20} | {Solution().countAndSay(n):<20} | OK={actual == str(ans)}')
