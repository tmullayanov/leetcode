class Solution:
    def duplicateZeros(self, arr):
        idx = 0
        l = len(arr)
        while idx < l:
            if arr[idx] != 0:
                idx += 1
                continue
            tmp_val = 0
            running_idx = idx + 1
            while running_idx < l:
                arr[running_idx], tmp_val = tmp_val, arr[running_idx]
                running_idx += 1
            idx += 2


if __name__ == '__main__':
    arrs = [
            [1, 0, 2, 0, 3, 0, 4, 0, 5, 0],
            [1, 2, 3]
    ]
    for arr in arrs:
        print(f'got {arr=}')
        Solution().duplicateZeros(arr)
        print(f'transformed into {arr=}')
