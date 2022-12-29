import unittest
import logging
import sys
from typing import *

log = logging.getLogger("TestLog")


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        elif n == 1:
            return ["()"]

        return self._genParenthesis(n)

    def _genParenthesis(self, n):
        initial = ("()" * n)  # ()()...() -> ... -> (((...)))
        l = 2 * n
        all_wellformed_parens = [initial]

        current = list(initial)
        while True:
            most_right_op_paren = l - 1
            while most_right_op_paren >= 0:
                if current[most_right_op_paren] == '(':
                    break
                else:
                    most_right_op_paren -= 1

            if (most_right_op_paren < 0):
                break  # shouldn't be reached

            closest_left_close_paren = most_right_op_paren
            while closest_left_close_paren >= 0:
                if current[closest_left_close_paren] == ')':
                    break
                else:
                    closest_left_close_paren -= 1

            if closest_left_close_paren <= 0:
                break

            current[closest_left_close_paren] = '('
            count = sum(
                1 if current[i] == '(' else -1 for i in range(closest_left_close_paren+1)
            )

            for i in range(closest_left_close_paren + 1, l):
                if count > 0:
                    current[i] = ')'
                    count -= 1
                else:
                    current[i] = '('
                    count += 1

            all_wellformed_parens.append(''.join(current))

        return all_wellformed_parens


class SolutionTest(unittest.TestCase):

    def test_zero(self):
        s = Solution()
        self.assertEqual(s.generateParenthesis(0), [])

    def test_trivia(self):
        s = Solution()
        self.assertTrue(self._compare_outputs(
            ["()"], s.generateParenthesis(1)))

    def test_n_equals_two(self):
        s = Solution()
        parens = 2
        au_output = ["()()", "(())"]
        output = s.generateParenthesis(parens)
        self.assertTrue(self._compare_outputs(output, au_output),
                        f'{output=} is not equal to {au_output=}')

    def test_n_equals_three(self):
        s = Solution()
        n = 3
        au_output = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        output = s.generateParenthesis(n)
        self.assertTrue(self._compare_outputs(output, au_output),
                        f'{output=} is not equal to {au_output=}')

    def _compare_outputs(self, lhs: List[str], rhs: List[str]) -> bool:
        if len(lhs) != len(rhs):
            return False

        unique_lhs, unique_rhs = set(lhs), set(rhs)
        return unique_lhs == unique_rhs


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    unittest.main()
