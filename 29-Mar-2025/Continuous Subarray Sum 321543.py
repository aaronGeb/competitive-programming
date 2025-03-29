# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0 : -1}
        prefix_sum =0
        for i, num in enumerate(nums):
            prefix_sum +=num
            mod = prefix_sum % k
            if mod not in remainder:
                remainder[mod] = i
            elif i - remainder[mod] >1:
                return True
        return False
        