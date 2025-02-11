# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        pair = sum(i//2 for i in count.values())
        leftover = sum(k%2  for k in count.values())
        return [pair,leftover]
        