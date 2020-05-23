class Solution:
    def intervalIntersection(self, A, B):
        if not A or not B:
            return []

        res = []

        a = A.pop(0)
        b = B.pop(0)
        while a and b:
            print(f'{a=} {b=}')
            b_starts_in_a = a[0] <= b[0] <= a[1]
            a_starts_in_b = b[0] <= a[0] <= b[1]

            if b_starts_in_a or a_starts_in_b:
                res.append([
                    max(a[0], b[0]), min(b[1], a[1])
                ])
                if b[1] < a[1]:
                    b = B.pop(0) if B else None
                elif b[1] > a[1]:
                    a = A.pop(0) if A else None
                else:
                    b = B.pop(0) if B else None
                    a = A.pop(0) if A else None
            elif a[0] < b[0]:
                # b comes later than a
                a = A.pop(0) if A else None
            else:
                b = B.pop(0) if B else None

        return res


if __name__ == '__main__':
    A = [[0, 2], [5, 10], [13, 23], [24, 25]]
    B = [[1, 5], [8, 12], [15, 24], [25, 26]]

    print(Solution().intervalIntersection(A, B))
    # exp [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
