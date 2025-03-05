# Problem: Minimum Average Difference - https://leetcode.com/problems/minimum-average-difference/

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        min_index = 0
        min_diff =  float(inf)
        n = len(nums)
        for i in range(n):
            left_sum += nums[i]
            left_avg = left_sum//(i+1)
            right_sum = total_sum - left_sum
            right_avg = right_sum//(n-i-1) if (n-1-i) >0 else 0
            avg_diff = abs(right_avg - left_avg)
            if avg_diff < min_diff:
                min_diff = avg_diff
                min_index = i
        return min_index