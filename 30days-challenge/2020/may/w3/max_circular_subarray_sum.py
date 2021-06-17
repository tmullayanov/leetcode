class Solution:
    def maxSubarraySumCircular(self, arr):
        total = 0
        max_sum = -float('inf')
        min_sum = float('inf')
        curr_max = curr_min = 0

        for n in arr:
            total += n
            curr_max = max(n, curr_max + n)
            max_sum = max(max_sum, curr_max)
            curr_min = min(n, curr_min + n)
            min_sum = min(curr_min, min_sum)
        return max(max_sum, total - min_sum) if max_sum >= 0 else max_sum


if __name__ == '__main__':
    tests = (
        (([1, -2, 3, -2],), 3),
        (([5, -3, 5],), 10),
        (([3, -1, 2, -1],), 4),
        (([3, -2, 2, -3],), 3),
        (([-2, -3, -1],), -1)
    )

    for args, exp in tests:
        actual = Solution().maxSubarraySumCircular(*args)
        print(f'{args=} {actual=} {exp=}')
