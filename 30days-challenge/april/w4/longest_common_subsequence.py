class Solution:
    def longestCommonSubsequence(self, text1, text2):
        if not text1 or not text2:
            return 0

        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i, x in enumerate(text1):
            for j, y in enumerate(text2):
                if x == y:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

        return dp[i + 1][j + 1]


if __name__ == '__main__':
    print(Solution().longestCommonSubsequence('abcde', 'ace'))  # 3
    print(Solution().longestCommonSubsequence('abcde', ''))  # 0
    print(Solution().longestCommonSubsequence('abcde', 'fgh'))  # 0

