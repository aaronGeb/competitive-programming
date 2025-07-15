# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for key,num in enumerate(nums):
            if key > max_reach:
                return False
            max_reach = max(max_reach,num+key)
        return True
