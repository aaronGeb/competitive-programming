# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        result = []
        for num in nums:
            if count[num] == 1:
                result.append(num)
        return result

        