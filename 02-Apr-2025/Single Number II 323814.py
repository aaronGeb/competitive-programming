# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        for i,val in enumerate(count):
            if count[val]< 3:
                return val
        