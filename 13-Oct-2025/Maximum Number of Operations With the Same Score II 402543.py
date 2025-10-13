# Problem: Maximum Number of Operations With the Same Score II - https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/description/

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def dp(l, r, target):
            if r - l + 1 < 2:
                return 0
            res = 0
            if nums[l] + nums[l + 1] == target:
                res = max(res, 1 + dp(l + 2, r, target))
            if nums[r] + nums[r - 1] == target:
                res = max(res, 1 + dp(l, r - 2, target))
            if nums[l] + nums[r] == target:
                res = max(res, 1 + dp(l + 1, r - 1, target))

            return res
        ans = 0
        ans = max(ans, 1 + dp(2, n - 1, nums[0] + nums[1]))
        ans = max(ans, 1 + dp(0, n - 3, nums[-1] + nums[-2]))
        ans = max(ans, 1 + dp(1, n - 2, nums[0] + nums[-1]))

        return ans