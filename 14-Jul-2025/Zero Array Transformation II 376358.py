# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        def can_zero_after_k_queries(k):
            diff = [0] * (n + 1)
            for l, r, val in queries[:k]:
                diff[l] += val
                if r + 1 < n:
                    diff[r + 1] -= val

            curr_sum = 0
            for i in range(n):
                curr_sum += diff[i]
                if nums[i] > curr_sum:
                    return False
            return True

        max_k = len(queries)
        k = bisect_left(range(max_k + 1), True, key=can_zero_after_k_queries)
        return -1 if k > max_k else k