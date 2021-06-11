from typing import *

'''
Array of N integers in the range [1, n] but some of them are missing.
List them.
'''


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # simple: make a set with distinct numbers from 1 to n
        # then iterate over an array and remove (remove-if-present) numbers
        # you get over iterations. But that requires O(n) additional memory and O(nlogn) time
        # better: we might get O(n) time if we use array of zeroes instead of set.
        # When we iterate over an array and see X value, we increase AdditionalArray[X-1] by 1.
        # then we have to list indexes (+1) which have zero value. Still O(n) memory.
        i, N = 0, len(nums)
        for i in range(len(nums)):
            while nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
        return [i for (i, elem) in enumerate(nums, 1) if i != elem]

    def findDisappearedExtraMemory(self, nums):
        includes = [0 for _ in range(len(nums))]
        for x in nums:
            includes[x-1] += 1
        res = [i for (i, elem) in enumerate(nums, 1) if elem == 0]

        return res


if __name__ == '__main__':

    tests = (
        ([1, 1], [2]),
        ([1, 2, 2, 3, 3, 4, 7, 8], [5, 6]),
        ([4, 3, 2, 7, 8, 2, 3, 1], [5, 6])
    )

    print('---------')
    for (test, answer) in tests:
        print(f'{test=} {answer=} solution={Solution().findDisappearedNumbers(test)}')
