# Problem: Maximal Score After Applying K Operations - https://leetcode.com/problems/maximal-score-after-applying-k-operations

import heapq as h
import math as m
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        maxHeap = [-num for num in nums]
        h.heapify(maxHeap)
        score =0
        for _ in range(k):
            max_val = -h.heappop(maxHeap)
            score += max_val
            h.heappush(maxHeap,-(m.ceil(max_val/3)))
        return score