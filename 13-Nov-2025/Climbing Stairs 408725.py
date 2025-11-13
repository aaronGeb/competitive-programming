# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(k):
            if k==0 or k==1:
                return 1
            if k in memo:
                return memo[k]
            memo[k] = dp(k-1) + dp(k-2)
            return memo[k]
        return dp(n)



        