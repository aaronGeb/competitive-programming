# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def is_too_small(distance: int) -> bool:
            last_pos = -inf
            count = 0
            for pos in position:
                if pos - last_pos >= distance:
                    last_pos = pos
                    count += 1
            return count < m

        left, right = 1, position[-1]
        return bisect_left(range(left, right + 1), True, key=is_too_small)