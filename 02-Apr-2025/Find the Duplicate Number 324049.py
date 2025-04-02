# Problem: Find the Duplicate Number - https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = Counter(nums)
        for num in nums:
            if count[num] >1:
                return num
        