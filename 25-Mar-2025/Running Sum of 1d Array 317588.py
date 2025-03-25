# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        s = 0
        for num in nums:
            s +=num
            running_sum.append(s)
        return running_sum
        