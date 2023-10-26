import unittest


class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        while n:
            a, b = b, a + b
            n -= 1
        return b

class ClimbingStairsTest(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_one_step(self):
        n = self.s.climbStairs(1)
        self.assertEqual(n, 1)

    def test_two_step(self):
        n = self.s.climbStairs(2)
        self.assertEqual(n, 2)

    def test_three_step(self):
        self.assertEqual(
            self.s.climbStairs(3),
            3
        )
    
    def test_n_steps(self):
        self.assertEqual(
            self.s.climbStairs(4),
            5
        )

        self.assertEqual(
            self.s.climbStairs(5),
            8
        )



if __name__ == '__main__':
    unittest.main()