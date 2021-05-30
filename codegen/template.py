class Solution:
    def TESTMETHOD(self):
        pass


if __name__ == '__main__':

    tests = (
        #(input, output)
    )

    for args, expected in tests:
        actual = Solution().TESTMETHOD(*args)
        stat = 'OK' if actual == expected else 'FAIL'
        print(f'args={args} actual={actual} expected={expected} ...{stat}')
