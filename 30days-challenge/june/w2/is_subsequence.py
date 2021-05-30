class Solution:
    def isSubsequence(self, s, t):
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(s)


if __name__ == '__main__':
    print(Solution().isSubsequence("abc", "ahbhgc"))
    print(Solution().isSubsequence("axc", "ahbgfc"))
