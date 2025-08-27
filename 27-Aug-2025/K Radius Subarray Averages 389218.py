# Problem: K Radius Subarray Averages - https://leetcode.com/problems/k-radius-subarray-averages/description/

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [-1] * n
        window_size = 2 * k + 1
        
        if window_size > n:
            return result  
        
        window_sum = sum(nums[:window_size])
        result[k] = window_sum // window_size
        
        for i in range(k + 1, n - k):
            window_sum += nums[i + k] - nums[i - k - 1]
            result[i] = window_sum // window_size
        
        return result
        