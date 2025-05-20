# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            diff = abs(num) - 1
            if nums[diff] > 0:
                nums[diff] *= -1
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]