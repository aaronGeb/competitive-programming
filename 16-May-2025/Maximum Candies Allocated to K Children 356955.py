# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left, right = 0, max(candies)
        while left < right:
            mid = (left + right + 1) >> 1
            if sum(i // mid for i in candies) >= k:
                left = mid
            else:
                right = mid - 1
        return left