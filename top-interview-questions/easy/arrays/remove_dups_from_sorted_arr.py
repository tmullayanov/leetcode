from typing import *


class Solution:
    # no inner loops
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        write_idx = 0
        for i in range(l):
            if nums[i] == nums[write_idx]:
                continue
            write_idx += 1
            if i > write_idx:
                nums[write_idx], nums[i] = nums[i], nums[write_idx]

        return write_idx + 1

    def removeDuplicates2(self, nums: List[int]) -> int:
        l = len(nums)
        idx = 0
        while idx < l - 1:
            if nums[idx] == nums[idx + 1]:
                for j in range(idx, l - 1):
                    nums[j] = nums[j + 1]
                l -= 1
                continue
            idx += 1
        return l


if __name__ == '__main__':
    tests = (
        [1, 2, 3, 3, 3, 4],
        [1, 2, 3, 4],
        [1, 1, 1, 1],
        [1],
        [1, 1, 2, 2, 3, 3, 3, 3, 3, 4, 6]
    )

    for test in tests:
        print(f'{test=}')
        method = Solution().removeDuplicates2
        k = method(test)
        print(f'{k=} answer={test}')
