# Problem: Find the Smallest Divisor Given a Threshold - https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def sum_div(n):
            return sum((num + n -1)//n for num in nums)
        left = 1
        right = max(nums)
        while left < right:
            mid = (left + right)//2
            if sum_div(mid) > threshold:
                left = mid +1
            else:
                right = mid
        return left