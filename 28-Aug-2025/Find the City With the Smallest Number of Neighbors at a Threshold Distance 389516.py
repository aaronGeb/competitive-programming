# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        def dijkstra_count(src: int) -> int:
            dist = [float('inf')] * n
            dist[src] = 0
            heap = [(0, src)]
            while heap:
                d, u = heapq.heappop(heap)
                if d > dist[u]:
                    continue
                if d > distanceThreshold:
                    continue
                for v, w in adj[u]:
                    nd = d + w
                    if nd < dist[v] and nd <= distanceThreshold:
                        dist[v] = nd
                        heapq.heappush(heap, (nd, v))
            cnt = 0
            for i in range(n):
                if i != src and dist[i] <= distanceThreshold:
                    cnt += 1
            return cnt

        best_city = -1
        best_count = float('inf')

        for city in range(n):
            cnt = dijkstra_count(city)
            if cnt < best_count or (cnt == best_count and city > best_city):
                best_count = cnt
                best_city = city

        return best_city
