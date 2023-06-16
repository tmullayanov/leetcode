import math
from collections import namedtuple

Test = namedtuple('Test', ['nums', 'k', 'ans'])


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        if k > n:
            k = k % n

        if k == 0 or k == n:  # = nums should stay the same
            return

        gcd = math.gcd(n, k)
        if gcd > 1:
            self._rotateWithCyclicDeps(nums, k, gcd)
        else:
            self._rotateWithoutCyclicDeps(nums, k)

    def _rotateSingleChain(self, nums: list[int], k: int, start: int):
        n = len(nums)
        cur = nums[start]
        idx = start
        while True:
            new_idx = (idx + k) % n

            tmp = nums[new_idx]
            nums[new_idx] = cur

            cur = tmp
            idx = new_idx

            if idx == start:
                break

    def _rotateWithoutCyclicDeps(self, nums: list[int], k: int):
        self._rotateSingleChain(nums, k, 0)

    def _rotateWithCyclicDeps(self, nums: list[int], k: int, times: int):
        for start in range(times):
            self._rotateSingleChain(nums, k, start)


if __name__ == '__main__':
    tests = (
        Test([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
        Test([1, 2, 3, 4, 5], 3, [3, 4, 5, 1, 2]),
        Test([1], 10, [1]),
        Test([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        Test([1, 2, 3, 4, 5, 6], 4, [3, 4, 5, 6, 1, 2])
    )

    for (nums, k, ans) in tests:
        print(f'rotate {nums=} by {k=}')
        Solution().rotate(nums, k)
        print(f'RESULT: {nums=} {ans=}\n')
        print('OK' if ans == nums else 'FAIL')
