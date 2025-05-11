# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(n: int) -> bool:
            return sum((i + n - 1) // n for i in piles) <= h

        return 1 + bisect_left(range(1, max(piles) + 1), True, key=check)