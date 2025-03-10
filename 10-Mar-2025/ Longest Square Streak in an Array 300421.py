# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        nums_set = set(nums)
        max_streak = -1
        for num in nums:
            streak = 1
            while num * num in nums_set:
                num *= num
                streak +=1
            if streak > 1:
                max_streak =    max(max_streak, streak)
        return max_streak
        