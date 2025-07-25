# Problem: Maximum Number of Consecutive Values You Can Make - https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/description/

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        current_sum = 0
        
        for coin in coins:
            if coin <= current_sum + 1:
                current_sum += coin
            else:
                break
        
        return current_sum + 1