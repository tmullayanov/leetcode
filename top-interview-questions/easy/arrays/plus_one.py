from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        cur_idx = len(digits) - 1
        digits[cur_idx] += 1
        while cur_idx >= 0 and digits[cur_idx] >= 10:
            digits[cur_idx] %= 10
            if cur_idx == 0:
                digits = [1] + digits
                break
            digits[cur_idx - 1] += 1
            cur_idx -= 1
        return digits


if __name__ == '__main__':
    tests = (
        ([1, 2, 3], [1, 2, 4]),
        ([4, 3, 2, 1], [4, 3, 2, 2]),
        ([0], [1]),
        ([9], [1, 0]),
        ([9, 9], [1, 0, 0])
    )

    for (test, ans) in tests:
        print(f'{test=} {ans=} solution={Solution().plusOne(test)}')
