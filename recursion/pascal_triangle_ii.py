class Solution:
    def getRow(self, rowIndex):
        row, cur = [1], 0

        while cur != rowIndex:
            next_row_len = len(row) + 1
            next_row = []
            for i in range(next_row_len):
                if i == 0 or i == next_row_len - 1:
                    next_row.append(1)
                else:
                    next_row.append(row[i] + row[i-1])
            row = next_row
            cur += 1

        return row


if __name__ == '__main__':
    tests = (
        ((0,), [1]),
        ((1,), [1, 1]),
        ((2,), [1, 2, 1]),
        ((3,), [1, 3, 3, 1]),
        ((4,), [1, 4, 6, 4, 1])
    )

    for args, expected in tests:
        actual = Solution().getRow(*args)
        ok = 'OK' if actual == expected else 'FAIL'
        print(f'args={args} actual={actual} expected={expected} {ok}')
