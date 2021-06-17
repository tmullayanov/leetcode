class Solution:
    def _min(self, a, b):
        if a is None and b is None: return 0
        if a is None: return b
        if b is None: return a
        return min(a, b)

    def minPathSum(self, grid):
        if not grid: return 0
        h = len(grid)
        w = len(grid[0])
        costs = [[0 for _ in range(w)] for _ in range(h)]

        for i in range(h):
            for j in range(w):
                prev = costs[i][j-1] if j > 0 else None
                upper = costs[i-1][j] if i > 0 else None
                costs[i][j] = self._min(prev, upper) + grid[i][j]
        return costs[h-1][w-1]


def pprint(table):
    for row in table:
        print(''.join(str(i).rjust(5) for i in row))


if __name__ == '__main__':
    grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
    print(Solution().minPathSum(grid))
