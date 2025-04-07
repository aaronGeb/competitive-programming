# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: 0 can always be formed

        for num in nums:
            for i in range(target, num - 1, -1):  # Go backwards to avoid overwriting
                dp[i] = dp[i] or dp[i - num]

        return dp[target]
