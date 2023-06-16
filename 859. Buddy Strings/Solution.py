class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal and len(s) > len(set(s)):
            return True

        different_sym_indices = [i for i in range(len(s)) if s[i] != goal[i]]

        if len(different_sym_indices) != 2:
            return False

        pos1, pos2 = different_sym_indices
        return s[pos1] == goal[pos2] and s[pos2] == goal[pos1]
        
        
if __name__ == '__main__':
    tests = (
        (("ab", "ba"), True),
        (("ab", "ab"), False),
        (("aa", "aa"), True),
        (("abc", "accc"), False)
    )
    
    for ((s, goal), res) in tests:
        print(f'{s=} {goal=}')
        ans = Solution().buddyStrings(s, goal)
        print(f'{ans=} expected={res} {"OK" if ans == res else "NOT OK"}')
