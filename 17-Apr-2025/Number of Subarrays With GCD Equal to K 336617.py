# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            current_gcd = 0
            for j in range(i,n):
                current_gcd = gcd(current_gcd, nums[j])
                if current_gcd <k:
                    break
                if current_gcd == k:
                    count += 1
        return count