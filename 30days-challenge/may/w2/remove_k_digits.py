class Solution:
    def removeKdigits(self, num, k):
        if len(num) <= k:
            return '0'
        stack = []
        for digit in num:
            while k > 0 and stack and int(stack[-1]) > int(digit):
                stack.pop()
                k -= 1
            stack.append(digit)
        while k > 0:
            stack.pop()
            k -= 1
        ans = ''.join(stack).lstrip('0')
        return ans if ans else '0'


if __name__ == '__main__':
    print(Solution().removeKdigits("1432219", 3))  # 129
    print(Solution().removeKdigits("10200", 1))  # 200
    print(Solution().removeKdigits("10", 2))  # 0
