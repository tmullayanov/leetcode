from typing import *


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        idx = 0
        while idx < l - 1:
            if nums[idx] == nums[idx + 1]:
                for i in range(idx, l - 1):
                    nums[i] = nums[i+1]
                l -= 1
                continue  # prevent multiple dups
            idx += 1
        return l


if __name__ == '__main__':
    tests = [
        [1, 1, 2],
        [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]
    ]

    for test in tests:
        print(Solution().removeDuplicates(test))
    print('------------')
    print(tests)
