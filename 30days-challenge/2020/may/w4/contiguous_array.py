class Solution:
    def findMaxLength(self, nums):
        _sum = 0
        ans = 0
        earliest_occurences = {0: 0}
        for i in range(len(nums)):
            _sum += 1 if nums[i] == 1 else -1
            if _sum in earliest_occurences:
                ans = max(ans, i + 1 - earliest_occurences[_sum])
            else:
                earliest_occurences[_sum] = i + 1
        return ans


if __name__ == '__main__':
    print(Solution().findMaxLength([0, 1, 0]))
    print(Solution().findMaxLength([0, 1]))
