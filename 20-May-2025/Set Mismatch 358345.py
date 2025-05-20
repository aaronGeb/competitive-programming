# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return [sum(nums) - sum(set(nums)), sum(range(1, n + 1)) - sum(set(nums))]
        