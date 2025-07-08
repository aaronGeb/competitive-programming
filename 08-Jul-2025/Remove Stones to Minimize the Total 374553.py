# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        import heapq as q
        max_heap = [- p for p in piles]
        heapq.heapify(max_heap)
        for _ in range(k):
            large_val = -q.heappop(max_heap)
            new_val = large_val//2
            q.heappush(max_heap, -(large_val-new_val))
        return -sum(max_heap)