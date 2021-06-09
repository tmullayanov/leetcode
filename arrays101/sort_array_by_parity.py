from typing import *


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res = []
        for elem in nums:
            if elem % 2 == 0:
                res.append(elem)
        for elem in nums:
            if elem % 2 != 0:
                res.append(elem)
        return res
