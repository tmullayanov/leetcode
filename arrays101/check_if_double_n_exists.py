from typing import List


class Solution:
    def checkIfExists(self, arr: List[int]) -> bool:
        '''
        Check if there is N for which M = 2 * N exists
        in ARR
        '''
        seen = set()
        for x in arr:
            if x % 2 == 0 and (x / 2) in seen:
                print(f'found {x=}')
                return True
            if (x * 2) in seen:
                print(f'found {x=}')
                return True
            seen.add(x)
        return False


if __name__ == '__main__':
    tests = (
        ([10, 2, 5, 3], True),
        ([7, 1, 14, 11], True),
        ([3, 1, 7, 11], False),
        ([-2, 0, 10, -19, 4, 6, -8], False)
    )

    for (arr, expected) in tests:
        res = Solution().checkIfExists(arr)
        print(f'{arr=} {res=} {expected=} OK={res==expected}')
