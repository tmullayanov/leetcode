class Solution:
    def rangeBitwiseAnd(self, m, n):
        import math

        if m == 0 or m == n:
            return m

        m_msb = math.floor(math.log(m, 2))
        n_msb = math.floor(math.log(n, 2))
        if m_msb != n_msb:
            return 0

        common = 2**m_msb
        return common + self.rangeBitwiseAnd(m-common, n-common)


if __name__ == '__main__':
    tests = [
        ((0, 2**31 - 1), 0),
        ((0, 1), 0),
        ((3, 3), 3),
        ((6, 7), 6),
        ((5, 7), 4)
    ]

    for (inp, outp) in tests:
        res = Solution().rangeBitwiseAnd(*inp)
        status = 'OK' if res == outp else 'FAIL'
        print(f'input={inp}. actual={res} expected={outp} status={status}')
