#!/usr/bin/env python3
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in mydict:
                return [mydict[diff], i]
            mydict[n] = i
        return
