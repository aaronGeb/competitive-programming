# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        des_sum = int(len(nums) *((len(nums) +1)) *0.5)
        missing_number = des_sum - total_sum
        return missing_number
        