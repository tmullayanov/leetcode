class Solution:
    def solve(self, board):
        if not board:
            return

        M, N = len(board), len(board[0])

        for i in range(M):
            self.dfs(board, i, 0)
            self.dfs(board, i, N - 1)

        for i in range(N):
            self.dfs(board, 0, i)
            self.dfs(board, M - 1, i)

        for i, j in ((i, j) for i in range(M) for j in range(N)):
            board[i][j] = 'X' if board[i][j] != 'T' else 'O'

    def dfs(self, board, x, y):
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] != 'O':
            return
        board[x][y] = 'T'
        self.dfs(board, x + 1, y)
        self.dfs(board, x, y + 1)
        self.dfs(board, x - 1, y)
        self.dfs(board, x, y - 1)


if __name__ == '__main__':
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
             ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    Solution().solve(board)
    print('\n'.join(''.join(k) for k in board))
