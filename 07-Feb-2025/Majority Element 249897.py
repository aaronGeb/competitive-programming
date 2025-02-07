# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        for key,value in count.items():
            if value > len(nums)/2:
                return key
        return

        