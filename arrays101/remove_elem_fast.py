from typing import *


class Solution:
    def removeElement(self, nums: List[int], val: int):
        l = len(nums)
        idx = 0
        while idx < l:
            if nums[idx] == val:
                # remove
                nums[idx] = nums[l-1]
                l -= 1
                continue
            idx += 1
        return l


if __name__ == '__main__':
    tests = [
        ([3, 2, 2, 3], 3),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2),
        ([0, 1, 2, 3, 4], 5)
    ]

    for (nums, val) in tests:
        print(Solution().removeElement(nums, val))
    print('------------')
    print('\n'.join(str(test) for test in tests))
