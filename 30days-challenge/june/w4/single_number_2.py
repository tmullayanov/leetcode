class Solution:
    def singleNumber(self, nums):
        ones = 0
        twos = 0
        for n in nums:
            twos |= ones & n
            ones ^= n
            # need to remove common bits from ones and twos
            distinct = ~(ones & twos)
            ones &= distinct
            twos &= distinct
        return ones


if __name__ == '__main__':
    print(Solution().singleNumber([1, 1, 1, 2]))
