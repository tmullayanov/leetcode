from typing import *


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]

        largest_idx = -1
        largest_elem = 0

        for cur_idx in range(len(arr)-1):
            if largest_idx == -1 or cur_idx >= largest_idx:
                largest_elem = 0
                for idx in range(cur_idx + 1, len(arr)):
                    if arr[idx] > largest_elem:
                        largest_idx = idx
                        largest_elem = arr[idx]
            arr[cur_idx] = largest_elem

        arr[len(arr) - 1] = -1
        return arr


if __name__ == '__main__':
    tests = (
        [17, 18, 5, 4, 6, 1],
        [400],
        [100, 50, 1],
        [100, 25, 24, 26, 25, 23, 20]
    )

    for test in tests:
        print(f'arr={test} solution={Solution().replaceElements(test)}')
