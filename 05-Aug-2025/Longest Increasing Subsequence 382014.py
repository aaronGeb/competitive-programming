# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for k in range(i):
                if nums[i] > nums[k]:
                    dp[i] = max(dp[i],dp[k]+1)
        return max(dp)