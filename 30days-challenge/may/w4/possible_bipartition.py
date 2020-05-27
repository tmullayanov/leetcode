class Solution:
    def possibleBipartition(self, N, dislikes):
        bipartite = {}
        queue = []
        graph = {}

        for edge in dislikes:
            u, v = edge
            graph[u] = graph.get(u, []) + [v]
            graph[v] = graph.get(v, []) + [u]

        for vertex in graph:
            if vertex in bipartite:
                continue

            bipartite[vertex] = True
            queue.append(vertex)
            while queue:
                next_v = queue.pop()
                if next_v not in graph:
                    continue

                for neighbor in graph[next_v]:
                    if neighbor in bipartite and bipartite[neighbor] == bipartite[next_v]:
                        return False
                    elif neighbor not in bipartite:
                        bipartite[neighbor] = not bipartite[next_v]
                        queue.append(neighbor)

        return True


if __name__ == '__main__':
    tests = (
        {
            'args': {'N': 4, 'dislikes': [[1, 2], [1, 3], [2, 4]]},
            'expected': True
        },
        {
            'args': {'N': 3, 'dislikes': [[1, 2], [1, 3], [2, 3]]},
            'expected': False
        },
        {
            'args': {'N': 5, 'dislikes': [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]},
            'expected': False
        },
        {
            'args': {'N': 3, 'dislikes': [[1, 2], [2, 3]]},
            'expected': True
        },
        {
            'args': {'N': 6, 'dislikes': [[1, 2], [2, 3]]},
            'expected': True
        },
        {
            'args': {
                'N': 10,
                'dislikes': [[4, 7], [4, 8], [5, 6], [1, 6], [3, 7], [2, 5], [5, 8], [1, 2], [4, 9], [6, 10], [8, 10], [3, 6], [2, 10], [9, 10], [3, 9], [2, 3], [1, 9], [4, 6], [5, 7], [3, 8], [1, 8], [1, 7], [2, 4]]
            },
            'expected': True
        }, {
            'args': {
                'N': 10,
                'dislikes': [[5, 9], [5, 10], [5, 6], [5, 7], [1, 5], [4, 5], [2, 5], [5, 8], [3, 5]]
            },
            'expected': True
        }
    )
    for test in tests:
        actual = Solution().possibleBipartition(**test['args'])
        stat = 'OK' if actual == test['expected'] else 'FAIL'
        print(
            f'args={test["args"]} {actual=} expected={test["expected"]} {stat=}')
