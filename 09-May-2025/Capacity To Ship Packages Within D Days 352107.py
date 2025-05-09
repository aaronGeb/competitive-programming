# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def is_valid(capacity: int) -> bool:
            current_load, days_needed = 0, 1
            for weight in weights:
                current_load += weight
                if current_load > capacity:
                    days_needed += 1
                    current_load = weight
            return days_needed <= days

        left, right = max(weights), sum(weights) + 1
        return left + bisect_left(range(left, right), True, key=is_valid)