# Problem: Number of Subarrays With LCM Equal to K - https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            current_lcm = 1
            for j in range(i, n):
                current_lcm = math.lcm(current_lcm, nums[j])
                if current_lcm > k:
                    break
                if current_lcm == k:
                    ans += 1
        return ans