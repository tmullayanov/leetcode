class Solution:
    def maxUncrossedLines(self, A, B):
        dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1], 1+dp[i-1][j-1])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[len(A)][len(B)]


if __name__ == '__main__':
    print(Solution().maxUncrossedLines(
        [1, 4, 2], [1, 2, 4]
    ))  # 2
    print(Solution().maxUncrossedLines(
        [2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]
    ))  # 3
    print(Solution().maxUncrossedLines(
        [1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]
    ))  # 2
