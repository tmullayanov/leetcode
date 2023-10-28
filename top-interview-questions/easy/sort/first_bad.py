import unittest
import math
from unittest import mock

isBadVersion = lambda x: True

class Solution:

    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        lo, high = 1, n
        mid = n // 2
        ans = -1
        while high >= lo:
            if isBadVersion(mid):
                ans = mid
                high = mid - 1
            else:
                lo = mid + 1
            mid = (lo + high) // 2
        return ans

class FirstBadVersionTest(unittest.TestCase):

    def test_one_version(self):
        global isBadVersion
        isBadVersion = mock.Mock(wraps=lambda x: x == 1)

        s = Solution()        
        self.assertEqual(s.firstBadVersion(1), 1)
        self.assertGreaterEqual(1, isBadVersion.call_count)

    def test_two_versions(self):
        global isBadVersion
        isBadVersion = mock.Mock(wraps=lambda x: x >= 1)
        
        s = Solution()
        self.assertEqual(s.firstBadVersion(2), 1)
        self.assertEqual(1, isBadVersion.call_count)

        isBadVersion = mock.Mock(wraps=lambda x: x >= 2)
        self.assertEqual(s.firstBadVersion(2), 2)
        self.assertLessEqual(isBadVersion.call_count, 2)

    def test_multiple_versions(self):
        global isBadVersion
        isBadVersion = mock.Mock(wraps=lambda x: x > 3)

        s = Solution()
        n = 8
        self.assertEqual(s.firstBadVersion(n), 4)
        self.assertLessEqual(isBadVersion.call_count, math.ceil(math.log2(n)) + 1)

if __name__ == '__main__':
    unittest.main()