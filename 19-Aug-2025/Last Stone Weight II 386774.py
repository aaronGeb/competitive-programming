# Problem: Last Stone Weight II - https://leetcode.com/problems/last-stone-weight-ii/description/

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total//2
        dp = [0]*(target+1)
        for v in stones:
            for j in range(target, v-1,-1):
                dp[j] = max(dp[j], dp[j-v]+v)
        return total-2 *dp[target]