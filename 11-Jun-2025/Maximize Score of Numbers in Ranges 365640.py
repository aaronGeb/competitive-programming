# Problem: Maximize Score of Numbers in Ranges - https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        intervals = [(s, s + d) for s in start]
        intervals.sort() 

        def is_valid(gap):
            chosen = []
            prev = -float('inf')
            for l, r in intervals:
                
                pick = max(l, prev + gap)
                if pick > r:
                    return False
                chosen.append(pick)
                prev = pick
            return True

        left, right = 0, max(start) + d  

        while left < right:
            mid = (left + right + 1) // 2  
            if is_valid(mid):
                left = mid
            else:
                right = mid - 1

        return left