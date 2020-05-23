'''
This problem might be solved exactly like april/w4/first_unique_number

That decision uses DLL (doubly linked list) of things currently considered unique
(so head of that DLL is first unique element) and two hash-tables:
one keeps all repeated characters and the other stores references to node in DLL corresponding
to element.

The one traverses over sequence and for each character does the following:
- if repeated[value] = True, skip
- if inDLL[value], then mark repeated[value] = True,
remove inDLL[value] from DLL (+ remove ref from inDLL table)
- else inDLL[value] = new Node(value) and this node is added to the end of DLL

The solution provides correct algorithm for stream processing

However, in this task it is not required to provide such level of
correctness. And the input is constrained by lowercase letters of English alphabet
'''
from collections import OrderedDict


class Solution:
    def firstUniqChar(self, s):
        if not s:
            return -1

        seen = set()
        unique = []

        for c in s:
            if c not in seen:
                seen.add(c)
                unique.append(c)
            else:
                if c in unique:
                    unique.remove(c)
        if unique:
            return s.index(unique[0])
        return -1


if __name__ == '__main__':
    tests = (
        (('leetcode',), 0),
        (('loveleetcode',), 2),
        (('',), -1),
        (('cc',), -1)
    )

    for (args, expected) in tests:
        actual = Solution().firstUniqChar(*args)
        stat = 'OK' if actual == expected else 'FAIL'
        print(f'args={args} actual={actual} expected={expected} ...{stat}')
