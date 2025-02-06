# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        n = len(nums)
        duplicates = []
        for i in range(1,n+1):
            if count[i] >1:
                duplicates.append(i)
        return duplicates
        