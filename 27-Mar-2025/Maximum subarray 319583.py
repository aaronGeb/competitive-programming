# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur,curmax = nums[0],nums[0]
        for num in nums[1:]:
            cur = max(num,cur+num)
            curmax = max(cur,curmax)
        return curmax
