# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        max_sum = 0
        seen = set()  
        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])  
                current_sum -= nums[left]  
                left += 1  
            # Add the new unique element to the window
            seen.add(nums[right])
            current_sum += nums[right] 
            max_sum = max(max_sum, current_sum)

        return max_sum

        