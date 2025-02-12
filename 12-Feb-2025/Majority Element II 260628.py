# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        count = Counter(nums)
        for key,value in count.items():
            if  value > n/3:
                result.append(key)
        return result


        