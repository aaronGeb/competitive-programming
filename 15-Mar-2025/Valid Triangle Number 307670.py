# Problem: Valid Triangle Number - https://leetcode.com/problems/valid-triangle-number/

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        for trip in range(2,n):
            left = 0
            right = trip -1
            while left < right:
                if nums[left] + nums[right] > nums[trip]:
                    count += (right - left)
                    right -=1
                else:
                    left += 1
        return count         