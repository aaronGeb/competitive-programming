# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        osum = 0
        for i in range(len(nums)):
            osum +=nums[i]
            res.append(osum)
        return res
