class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        tbl = {}
        for sym in J:
            tbl[sym] = 0

        for sym in S:
            if sym in J:
                tbl[sym] += 1

        return sum(v for v in tbl.values())


if __name__ == '__main__':
    print(Solution().numJewelsInStones('aA', 'aAAbbbb'))
    print(Solution().numJewelsInStones('z', 'ZZ'))
