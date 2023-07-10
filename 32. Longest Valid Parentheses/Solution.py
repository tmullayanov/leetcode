class Solution:
  def longestValidParentheses(self, s: str) -> int:
    if not s:
        return 0
    _max = 0

    stack = []

    brackets = [0 for _ in s] # 1 if brackets[i] is matched, 0 otherwise
    for (i, c) in enumerate(s):
      if c == '(':
        stack.append(i)
      else:
        if stack:
          top = stack.pop()
          brackets[i] = 1
          brackets[top] = 1

    _cur = 0
    for b in brackets:
      if b == 0:
        _max = max(_max, _cur)
        _cur = 0
      else:
        _cur += 1
    
    return max(_max, _cur)


if __name__ == '__main__':
  tests = (
    ('((()))', 6),
    (')))', 0),
    ('(((', 0),
    ('', 0),
    (')()())', 4),
    ('(()', 2),
    ('(())))()(())', 6),
    ('((()))))()()', 6),
    ('()(()', 2)    
  )

  for (s, expected) in tests:
    answer = Solution().longestValidParentheses(s)
    ok = answer == expected
    print(f'===\n{s=} {expected=} {answer=} {"OK" if ok else "FAIL"}')
