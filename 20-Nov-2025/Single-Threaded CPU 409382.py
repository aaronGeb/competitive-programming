# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        indexed = sorted([(et, pt, i) for i, (et, pt) in enumerate(tasks)], key=lambda x: x[0])
        
        result = []
        heap = []  
        time = 0
        i = 0
        
        while len(result) < n:
            while i < n and indexed[i][0] <= time:
                et, pt, idx = indexed[i]
                heapq.heappush(heap, (pt, idx))
                i += 1
            
            if heap:
                pt, idx = heapq.heappop(heap)
                time += pt
                result.append(idx)
            else:
                time = indexed[i][0]
        
        return result