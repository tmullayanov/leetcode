import math


def maxSubarray(nums):
    ans = nums[0]
    min_sum = 0
    _sum = 0

    for n in nums:
        _sum += n
        ans = max(ans, _sum - min_sum)
        min_sum = min(min_sum, _sum)
    return ans


if __name__ == '__main__':
    print(maxSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # expected 6
    print(maxSubarray([1, 2, 3, -1]))  # expected: 6
    print(maxSubarray([10, -5]))  # expected: 10
    print(maxSubarray([10, -20]))  # expected 10
    print(maxSubarray([-1]))  # expected -1
    print(maxSubarray([-2, -1]))  # expected -1
