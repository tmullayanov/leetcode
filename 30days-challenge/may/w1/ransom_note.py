class Solution:
    def canConstruct(self, ransomNote, magazine):
        ransomChars = {}
        magazineChars = {}
        for sym in ransomNote:
            ransomChars[sym] = ransomChars.get(sym, 0) + 1

        for sym in magazine:
            ransomChars[sym] = ransomChars.get(sym, 0) - 1

        return all(ransomChars[k] <= 0 for k in ransomChars)


if __name__ == '__main__':
    tests = [
        (('a', 'b'), False),
        (('aa', 'ab'), False),
        (('aa', 'aab'), True)
    ]

    for test in tests:
        inp, outp = test
        assert Solution().canConstruct(*inp) == outp
