# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            y = heapq.heappop(max_heap)
            x = heapq.heappop(max_heap)
            
            if y != x:
                heapq.heappush(max_heap, y - x)
        if not max_heap:
           
            return 0
        else:
            
            return -max_heap[0]

        