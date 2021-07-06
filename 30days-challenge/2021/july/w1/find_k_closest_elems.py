from typing import *


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # find idx to insert x into arr without actually inserting it
        insert_idx = self.find_insertion_idx(arr, x)
        print(f'{insert_idx=}')
        return []

    def find_insertion_idx(self, arr, x):
        if not len(arr) or not arr:
            return 0
        left, right = 0, len(arr) - 1
        mid = (left + right) // 2
        while left + 1 < right:
            print(f'{left=} {right=} {mid=}')
            if x < arr[mid]:
                right = mid
                mid = (left + right) // 2
            elif x > arr[mid]:
                left = mid
                mid = (left + right) // 2
            else:
                return mid
        print(f'{x=} {arr=} left={arr[left]} right={arr[right]}')
        return left if x <= arr[left] else right


if __name__ == '__main__':
    tests = (
        ([1, 2, 3, 4, 5], 4, 3),
        ([1, 2, 3, 4, 5], 4, 2.5),
        ([1, 2, 3, 4, 5], 4, -1)
    )

    for (arr, k, x) in tests:
        print(f'{arr=} {k=} {x=} ans={Solution().findClosestElements(arr, k, x)}')
