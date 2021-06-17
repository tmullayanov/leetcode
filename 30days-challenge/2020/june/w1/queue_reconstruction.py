class Solution:
    def reconstructQueue(self, people):
        result = []
        people.sort(key=lambda a: (-a[0], a[1]))
        for x in people:
            result.insert(x[1], x)
        return result


if __name__ == '__main__':
    print(
        Solution().reconstructQueue(
            [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
    )
