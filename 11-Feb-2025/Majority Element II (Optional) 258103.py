# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        count = Counter(nums)
        for key,value in count.items():
            if  value > n/3:
                result.append(key)
        return result


        