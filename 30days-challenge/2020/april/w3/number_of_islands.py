def parse_grid(grid):
    return [list(i.strip()) for i in filter(None, grid.split('\n'))]


def number_of_islands(raw_grid):
    def dfs(i, j):
        nonlocal grid, vertex_statuses, non_visited
        exists = 0 <= i < len(grid) and 0 <= j < len(grid[i])
        def is_water(r, c): return grid[r][c] == '0'

        if not exists or is_water(i, j) or vertex_statuses[(i, j)] == 1:
            return

        vertex_statuses[(i, j)] = 1
        non_visited.remove((i, j))

        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    grid = parse_grid(raw_grid)
    vertex_statuses = {}
    non_visited = set()
    count = 0
    # init: read all map and remember where land is
    for (row_idx, row) in enumerate(grid):
        for (col_idx, col) in enumerate(row):
            if col == '1':
                vertex_statuses[(row_idx, col_idx)] = 0
                non_visited.add((row_idx, col_idx))

    # while non_visited:
    #     count += 1
    #     # take element (we don't care which one) without removing it
    #     i, j = min(non_visited)
    #     print(f'log:: extracted ({i}, {j})')
    #     dfs(i, j)
    for (row_idx, row) in enumerate(grid):
        for (col_idx, col) in enumerate(row):
            if col == '1' and vertex_statuses[(row_idx, col_idx)] == 0:
                count += 1
                dfs(row_idx, col_idx)

    return count


grids = [
    '''
11000
10000
00010
    ''',
    '''
11111
00000
''',
    '''
101010
010101
'''
]

if __name__ == '__main__':
    for grid in grids:
        print(number_of_islands(grid))
