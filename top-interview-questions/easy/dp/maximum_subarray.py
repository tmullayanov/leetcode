import unittest
import math
from typing import *


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _max = nums[0]
        min_partial_sum = 0
        partial_sum = 0

        for n in nums:
            partial_sum += n
            _max = max(_max, partial_sum - min_partial_sum)
            min_partial_sum = min(partial_sum, min_partial_sum)

        return _max


class MaximumSubarrayTest(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_nothing(self):
        self.assertTrue(True)

    def test_single_elem_list(self):
        lists = [[1], [2]]
        for l in lists:
            self.assertEqual(l[0], self.s.maxSubArray(l))

    def test_positive_lists(self):
        l2 = [1, 2]
        self.assertEqual(3, self.s.maxSubArray(l2))
        l3 = [1, 2, 3]
        self.assertEqual(6, self.s.maxSubArray(l3))

    def test_2elem_neg_lists(self):
        l1 = [1, -2]
        self.assertEqual(1, self.s.maxSubArray(l1))

        l2 = [-2, 1]
        self.assertEqual(1, self.s.maxSubArray(l2))

        l3 = [-1, -2]
        self.assertEqual(-1, self.s.maxSubArray(l3))

    def test_leetcode_cases(self):
        l = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(6, self.s.maxSubArray(l))

        l2 = [5, 4, -1, 7, 8]
        self.assertEqual(23, self.s.maxSubArray(l2))


if __name__ == "__main__":
    unittest.main()
