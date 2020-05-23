# naive bruteforce: O(n^3)
# generate all subarrays(O(n^2)) + sum each (O(n))


def subarraySumNaive(nums, k):
    solutions_found = 0
    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            if sum(nums[i:j]) == k:
                solutions_found += 1
    return solutions_found

# bruteforce with prefix sum


def subarraySumPrefix(nums, k):
    solutions_found = 0
    prefixes, _sum = [], 0
    for elem in nums:
        _sum += elem
        prefixes.append(_sum)

    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            if prefixes[j] - prefixes[i] == k:
                solutions_found += 1
    return solutions_found


def subarraySumInPlace(nums, k):
    solutions_found = 0
    for i in range(0, len(nums)):
        s = 0
        for j in range(i, len(nums)):
            s += nums[j]
            if s == k:
                solutions_found += 1


def subarraySum(nums, k):
    solutions_found = 0
    sum_counts = {0: 1}
    _sum = 0
    for i in range(0, len(nums)):
        _sum += nums[i]
        diff = _sum - k
        if diff in sum_counts.keys():
            solutions_found += sum_counts[diff]  # check if correct
        sum_counts[_sum] = sum_counts.get(_sum, 0) + 1
    return solutions_found


if __name__ == '__main__':
    print(subarraySum([1, 1, 1], 2))
    print(subarraySum([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0))
