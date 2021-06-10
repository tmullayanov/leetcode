from typing import *


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        elif len(nums) == 3:
            return min(nums)
        # otherwise we have to do some real work
        arr = [*nums]
        N = len(arr)
        # import pdb
        # pdb.set_trace()
        return self.select(arr, 0, N - 1, 3)

    def partition(self, arr, start, end):
        x = arr[end]
        i = start - 1
        for j in range(start, end):
            if arr[j] >= x:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[end] = arr[end], arr[i + 1]
        return i + 1

    def select(self, arr, start, end, i):
        if start == end:
            return arr[start]
        pivot = self.partition(arr, start, end)
        k = pivot - start + 1
        if i == k:
            return arr[pivot]
        elif i < k:
            return self.select(arr, start, pivot - 1, i)
        else:
            return self.select(arr, pivot + 1, end, i - k)


if __name__ == '__main__':
    tests = (
        [3, 2, 1],
        [1, 2],
        [1],
        [2, 2, 3, 1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1, 3, 2, 6, 5, 4, 7]
    )
    # tests = (
    #     [1, 2, 3, 4, 5],
    # )

    for test in tests:
        print(f'{test=} answer={Solution().thirdMax(test)}')
