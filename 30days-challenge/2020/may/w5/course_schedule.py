class Solution:
    def canFinish(self, numCourses, preRequisites):
        self.graph = {k: [] for k in range(numCourses)}

        for pre, post in preRequisites:
            self.graph[pre].append(post)

        visited = [False] * numCourses
        inCurrentPath = [False] * numCourses
        for n in range(numCourses):
            if not visited[n]:
                if not self.dfs(self.graph, n, visited, inCurrentPath):
                    return False
        return True

    def hasCycle(self, node, visited, inCurrentPath):
        visited[node] = True
        inCurrentPath[node] = True

        for n in self.graph[node]:
            if inCurrentPath[n]:
                return True
            elif not visited[n]:
                if self.hasCycle(n, visited, inCurrentPath):
                    return True

        inCurrentPath[node] = False
        return False

    def dfs(self, graph, v, visited, path):
        path[v] = True
        visited[v] = True

        for n in graph[v]:
            if path[n]:
                return False
            elif not visited[n]:
                if not self.dfs(graph, n, visited, path):
                    return False

        path[v] = False
        return True


if __name__ == '__main__':
    print(Solution().canFinish(2, [[1, 0]]))  # True
    print(Solution().canFinish(2, [[1, 0], [0, 1]]))  # False
    print(Solution().canFinish(
        4, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]))  # True
    print(Solution().canFinish(
        4, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3], [3, 2]]))  # False
