from typing import *


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = {}
        for word in strs:
            _hash = ''.join(sorted(word))
            buckets[_hash] = buckets.get(_hash, []) + [word]
        return list(buckets.values())
