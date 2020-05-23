from collections import defaultdict


class Solution:
    def findJudge(self, N, trust):
        number_of_trusters = defaultdict(lambda: 0)
        non_trusters = set(range(1, N+1))
        for lhs, rhs in trust:
            number_of_trusters[rhs] += 1
            if lhs in non_trusters:
                non_trusters.remove(lhs)
        if len(non_trusters) != 1:
            return -1
        judge_candidate = non_trusters.pop()
        is_judge = number_of_trusters[judge_candidate] == N - 1
        return judge_candidate if is_judge else -1


if __name__ == '__main__':
    examples = [{
        'args': {
            'N': 2,
            'trust': [[1, 2]]
        },
        'expected': 2
    }, {
        'args': {
            'N': 3,
            'trust': [[1, 3], [2, 3]]
        },
        'expected': 3
    }, {
        'args': {
            'N': 3,
            'trust': [[1, 3], [2, 3], [3, 1]]
        },
        'expected': -1
    }, {
        'args': {
            'N': 3,
            'trust': [[1, 2], [2, 3]]
        },
        'expected': -1
    }]

    for testcase in examples:
        actual = Solution().findJudge(**testcase['args'])
        expected = testcase['expected']
        print(f'args={testcase["args"]} actual={actual} expected={expected}')
