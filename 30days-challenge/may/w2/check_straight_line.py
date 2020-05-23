class Solution:
    def areVectorsCollinear(self, v1, v2):
        a, b = v1
        c, d = v2
        return (a * d - b * c) == 0

    def makeVector(self, p1, p2):
        return [p2[0] - p1[0], p2[1] - p1[1]]

    def checkStraightLine(self, coordinates) -> bool:
        if len(coordinates) == 2:
            return True

        start, p1 = coordinates[:2]
        v0 = self.makeVector(start, p1)
        return all(
            self.areVectorsCollinear(v0, self.makeVector(start, p)) for p in coordinates[2:]
        )


if __name__ == '__main__':
    straight_line0 = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    print(Solution().checkStraightLine(straight_line0))

    two_dots = [[1, 2], [5, 9]]
    print(Solution().checkStraightLine(two_dots))

    curve = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
    print(Solution().checkStraightLine(curve))
