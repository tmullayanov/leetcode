from typing import *


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        low, high = 0, n
        while low < high:
            mid = (low + high) // 2
            tail = n - mid
            if citations[mid] >= tail:
                high = mid
            else:
                low = mid + 1
        return n - low


if __name__ == '__main__':
    print(Solution().hIndex([]))  # 0
    print(Solution().hIndex([10]))  # 1
    print(Solution().hIndex([0, 1, 3, 4, 6]))  # 3
    print(Solution().hIndex([0, 1, 1, 4, 6]))  # 3
