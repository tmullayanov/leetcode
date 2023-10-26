import unittest


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 1:
            return 0
        
        min_ind = None
        max_ind = None
        last_profit = 0
        
        for (i, p) in enumerate(prices):
            if min_ind is None or p < prices[min_ind]:
                min_ind = i
                max_ind = None
            if max_ind is None or p > prices[max_ind]:
                max_ind = i
                last_profit = max(last_profit, prices[max_ind] - prices[min_ind])
        return last_profit

class BestTimeStockTest(unittest.TestCase):
    def test_single_day(self):
        s = Solution()
        self.assertEqual(
            s.maxProfit([1]),
            0
        )

    def test_two_days(self):
        s = Solution()
        self.assertEqual(
            s.maxProfit([1, 2]),
            1
        )

        self.assertEqual(
            s.maxProfit([2, 1]),
            0
        )

        self.assertEqual(
            s.maxProfit([1, 1]),
            0
        )

    def test_three_days(self):
        s = Solution()
        self.assertEqual(
            s.maxProfit([1, 2, 3]),
            2
        )
        self.assertEqual(
            s.maxProfit([1, 3, 2]),
            2
        )
        self.assertEqual(
            s.maxProfit([3, 1, 2]),
            1
        )
        self.assertEqual(
            s.maxProfit([3, 2, 1]),
            0
        )
    
    def test_multiple_days(self):
        s = Solution()
        self.assertEqual(
            s.maxProfit([1, 2, 3, 4]),
            3
        )
        self.assertEqual(
            s.maxProfit([4, 3, 2, 1]),
            0
        )
        self.assertEqual(
            s.maxProfit([2, 4, 3, 1]),
            2
        )
        self.assertEqual(
            s.maxProfit([2, 1, 4, 3]),
            3
        )

        self.assertEqual(
            s.maxProfit([2, 4, 100, 300, 299, 298, 1]),
            298
        )

    def test_leetcode_examples(self):
        s = Solution()
        self.assertEqual(
            s.maxProfit([7,1,5,3,6,4]),
            5
        )
        self.assertEqual(
            s.maxProfit([7,6,4,3,1]),
            0
        )

if __name__ == '__main__':
    unittest.main()