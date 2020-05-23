class Solution:
    def findComplement(self, n):
        if n == 0:
            return 1
        if n & (n - 1) == 0:
            return n - 1

        import math
        return (2**math.ceil(math.log(n, 2)) - 1) ^ n


if __name__ == '__main__':
    tests = (
        ((5,), 2),
        ((7,), 0),
        ((10,), 5),
        ((1,), 0),
        ((2,), 1),
        ((4,), 3)
    )

    for (args, expected) in tests:
        actual = Solution().findComplement(*args)
        ok = 'OK' if actual == expected else 'FAIL'
        print(f'input={args} actual={actual} expected={expected} {ok}')
