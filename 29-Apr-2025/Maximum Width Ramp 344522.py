# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for i, val in enumerate(nums):
            if not stack or nums[stack[-1]] > val:
                stack.append(i)
        result = 0
        n = len(nums)
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                result = max(result, i - stack.pop())
            if not stack:
                break
        return result
        