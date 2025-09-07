# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/description/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n <2:
            return 0
        nums.sort()
        gap = 0
        for i in range(1,n):
            if nums[i] - nums[i-1] > gap:
                gap = nums[i] - nums[i-1]
        return gap
