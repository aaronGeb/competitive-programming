# Problem: Minimize Maximum of Array - https://leetcode.com/problems/minimize-maximum-of-array/

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = 0
        prefix_sum = 0
        
        for i, x in enumerate(nums):
            prefix_sum += x
            # ceiling of average of first i+1 elements
            avg = math.ceil(prefix_sum / (i + 1))
            ans = max(ans, avg)
        
        return ans