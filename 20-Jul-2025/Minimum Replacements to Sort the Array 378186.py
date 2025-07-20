# Problem: Minimum Replacements to Sort the Array - https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
   
        n = len(nums)
        operations = 0
        max_allowed = nums[-1]

        for i in range(n - 2, -1, -1):
            if nums[i] > max_allowed:
                parts = (nums[i] + max_allowed - 1) // max_allowed
                operations += parts - 1
                max_allowed = nums[i] // parts
            else:
                max_allowed = nums[i]

        return operations
