# Problem: Patching Array - https://leetcode.com/problems/patching-array/

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        _sum = 1
        idx = 0
        min_patch = 0

        while _sum <= n:
            if idx < len(nums) and nums[idx] <= _sum:
                _sum += nums[idx]
                idx += 1
            else:
                _sum *= 2
                min_patch += 1

        return min_patch