class Solution:
    def maximalSquare(self, matrix):
        if not matrix or len(matrix) == 0:
            return 0

        prev = 0
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [0 for _ in range(cols + 1)]
        maxSqLen = 0

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                tmp = dp[j]
                if matrix[i-1][j-1] == '1':
                    dp[j] = min(dp[j], dp[j-1], prev) + 1
                    maxSqLen = max(maxSqLen, dp[j])
                else:
                    dp[j] = 0
                prev = tmp
        return maxSqLen ** 2


if __name__ == '__main__':
    m = [
        ['1', '0', '1', '0', '0'],
        ['1', '0', '1', '1', '0'],
        ['1', '1', '1', '1', '1'],
        ['1', '0', '0', '1', '0']
    ]
    print(Solution().maximalSquare(m))
