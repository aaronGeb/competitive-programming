# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max_dist = 0
        min_val = arrays[0][0]
        max_val = arrays[0][-1]

        for i in range(1, len(arrays)):
            current_min = arrays[i][0]
            current_max = arrays[i][-1]

            max_dist = max(max_dist,abs(current_max - min_val),abs(max_val - current_min))
            min_val = min(min_val, current_min)
            max_val = max(max_val, current_max)

        return max_dist

        