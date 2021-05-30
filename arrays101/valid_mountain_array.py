from typing import *


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        going_up = True
        if not arr:
            return False
        for idx in range(len(arr) - 1):
            if going_up:
                if arr[idx] < arr[idx + 1]:
                    continue
                elif arr[idx] == arr[idx + 1]:
                    return False
                else:  # >, hit the pinnacle
                    if idx == 0:  # mustn't be at the start of arr
                        return False
                    going_up = False  # hit the pinnacle
            else:
                if arr[idx] <= arr[idx + 1]:
                    return False
        return not going_up


if __name__ == '__main__':
    tests = (
        ([2, 1], False),
        ([0, 3, 2, 1], True),
        ([3, 5, 5], False),
        ([3, 5, 6, 5, 5], False),
        ([], False),
        ([1, 2, 3, 4, 3, 2, 1], True),
        ([1, 2, 3, 4], False),
        ([4, 3, 2, 1], False),
        ([1, 1, 2, 3, 4, 3, 2, 1], False)
    )

    for (arr, exp) in tests:
        res = Solution().validMountainArray(arr)
        print(f'{arr=} {exp=} {res=} OK={exp==res}')
