from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str):
        res = []
        if len(s) < len(p):
            return res

        start = 0
        pCount = Counter(p)
        sCount = Counter(s[start:len(p)-1])
        for end in range(len(p) - 1, len(s)):
            sCount[s[end]] += 1
            if sCount == pCount:
                res.append(start)
            sCount[s[start]] -= 1
            if sCount[s[start]] == 0:
                del sCount[s[start]]
            start += 1
        return res


if __name__ == '__main__':
    tests = (
        ({
            "s": "cbaebabacd",
            "p": "abc"
        }, [0, 6]),
        ({
            "s": "abab",
            "p": "ab"
        }, [0, 1, 2]),
        ({
            "s": "abacaaba",
            "p": "aab"
        }, [0, 4, 5]),
        ({
            "s": "abacbabc",
            "p": "abc"
        }, [1, 2, 3, 5])
    )

    for kwargs, expected in tests:
        actual = Solution().findAnagrams(**kwargs)
        stat = 'OK' if actual == expected else 'FAIL'
        print(f'{kwargs=} {actual=} {expected=} {stat=}')
