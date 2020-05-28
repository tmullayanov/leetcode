class Solution:
    def countBits(self, num):
        res = []
        c = 0
        while c <= num:
            if c == 0 or c == 1:
                res.append(c)
            else:
                bits = 1 + res[c & (c - 1)]
                res.append(bits)
            c += 1
        return res


if __name__ == '__main__':
    print(Solution().countBits(17))
