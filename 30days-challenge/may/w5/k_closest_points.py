class Solution:
    def kClosest(self, points, k):
        sorted_points = sorted(points, key=lambda x: x[0]**2 + x[1]**2)
        return sorted_points[:k]


if __name__ == '__main__':
    print(Solution().kClosest(
        [[1, 3], [-2, 2]], 1
    ))  # [[-2, 2]]

    print(Solution().kClosest(
        [[3, 3], [5, -1], [-2, 4]], 2
    ))  # [[3, 3], [-2, 4]]
