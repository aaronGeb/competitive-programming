# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        for num in nums:
            if count[num] == 1:
                return num
            
        