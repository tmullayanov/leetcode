from typing import *


class Solution:
    WIDTH = 9
    HEIGHT = 9

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(Solution.HEIGHT):
            nums = [x for x in board[i] if x != '.']
            if self.hasDuplicates(nums):
                return False

        for i in range(Solution.WIDTH):
            nums = [board[j][i]
                    for j in range(Solution.HEIGHT) if board[j][i] != '.']
            if self.hasDuplicates(nums):
                return False

        for i in range(0, Solution.HEIGHT, 3):
            for j in range(0, Solution.WIDTH, 3):
                fields = board[i][j:j+3] + \
                    board[i+1][j:j+3] + board[i+2][j:j+3]
                nums = [x for x in fields if x != '.']
                if self.hasDuplicates(nums):
                    return False

        return True

    def hasDuplicates(self, nums: List[str]) -> bool:
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False


if __name__ == '__main__':
    board0 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(f'board0: expected=true actual={Solution().isValidSudoku(board0)}')
    print('-------------')
    board1 = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(f'board1: expected=false actual={Solution().isValidSudoku(board1)}')
    print('-----------')
    board2 = [
        [".", ".", "4", ".", ".", ".", "6", "3", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["5", ".", ".", ".", ".", ".", ".", "9", "."],
        [".", ".", ".", "5", "6", ".", ".", ".", "."],
        ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
        [".", ".", ".", "7", ".", ".", ".", ".", "."],
        [".", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."]]
    print(f'board2: expected=false actual={Solution().isValidSudoku(board2)}')
