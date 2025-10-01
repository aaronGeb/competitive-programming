# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))
        
        heap = [(0, k)]
        dist = {}  
        
        while heap:
            time, node = heapq.heappop(heap)
            if node in dist:
                continue
            dist[node] = time
            for neighbor, w in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(heap, (time + w, neighbor))
        
        if len(dist) != n:
            return -1
        return max(dist.values())