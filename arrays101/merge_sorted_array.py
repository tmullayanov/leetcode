from typing import *


class Solution:
    def merge(self, nums1, m, nums2, n):
        print('-------------------')
        run_idx1, run_idx2 = 0, 0
        while run_idx1 < (m + run_idx2) and run_idx2 < n:
            if nums1[run_idx1] < nums2[run_idx2]:
                run_idx1 += 1
            else:
                t = nums2[run_idx2]
                print(f'PASTING {t=} into {nums1=} starting from {run_idx1=}')
                for swap_idx in range(run_idx1, m + run_idx2 + 1):
                    nums1[swap_idx], t = t, nums1[swap_idx]
                    print(f'PASTE ENDLOOP {nums1=}')
                print(f'AFTER PASTE {nums1=}')
                run_idx2 += 1
            print(f'ENDLOOP {nums1=} {nums2=} {run_idx1=} {run_idx2=}')
        if run_idx2 < n:
            for t in range(run_idx2, n):
                nums1[run_idx1 + t - run_idx2] = nums2[t]


if __name__ == '__main__':
    tests = [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3),
        ([1], 1, [], 0),
        ([2, 3, 5, 0, 0, 0], 3, [0, 1, 2], 3),
        ([0, 5, 6, 0, 0, 0], 3, [0, 1, 4], 3),
        ([0, 1, 2, 3, 0, 0], 4, [10, 20], 2),
        ([0], 0, [1], 1),
    ]

    for (nums1, m, nums2, n) in tests:
        Solution().merge(nums1, m, nums2, n)
    print('---------------')
    print('\n'.join(str(test) for test in tests))
