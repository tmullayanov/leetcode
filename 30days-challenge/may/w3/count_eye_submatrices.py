class Solution:
    def countSquares(self, matrix):
        count = 0
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0 for _ in range(cols)] for __ in range(rows)]
        for i in range(cols):
            dp[0][i] = matrix[0][i]
            count += matrix[0][i]
        for i in range(1, rows):
            dp[i][0] = matrix[i][0]
            count += matrix[i][0]

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    left, up, diag = dp[i][j-1], dp[i-1][j], dp[i-1][j-1]
                    dp[i][j] = min(left, up, diag) + 1
                    count += dp[i][j]
        return count


if __name__ == '__main__':
    a = [
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1]
    ]
    print(Solution().countSquares(a))  # 15

    b = [
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 0]
    ]
    print(Solution().countSquares(b))  # 7
