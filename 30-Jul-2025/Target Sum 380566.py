# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if total < target or (total - target) % 2:
            return 0
        n = (total - target) // 2
        dp = [0] * (n + 1)
        dp[0] = 1
        for num in nums:
            for j in range(n, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[n]