class Solution:
    def checkValidString(self, s: str) -> bool:
        min_op = 0
        max_op = 0

        for c in s:
            min_op += 1 if c == "(" else -1
            max_op += -1 if c == ")" else 1
            if max_op < 0:
                return False
            min_op = max(min_op, 0)

        return min_op == 0


if __name__ == "__main__":
    tests = {
        True: ("()", "(())", "()()", "(*)", "(*))", "((*)"),
        False: (")()", ")(", "(*)))", "((())", "((((*)"),
    }

    for expected, strings in tests.items():
        for s in strings:
            print(f"{s=} ans={Solution().checkValidString(s)} {expected=}")
