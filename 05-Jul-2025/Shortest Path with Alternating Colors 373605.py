# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # Build adjacency lists
        red_adj = defaultdict(list)
        blue_adj = defaultdict(list)

        for u, v in redEdges:
            red_adj[u].append(v)
        for u, v in blueEdges:
            blue_adj[u].append(v)

        result = [-1] * n

        queue = deque()
        queue.append((0, 0, -1))  
        visited = set()  

        while queue:
            node, dist, last_color = queue.popleft()

            if result[node] == -1:
                result[node] = dist

            if last_color != 0:
                for nei in red_adj[node]:
                    if (nei, 0) not in visited:
                        visited.add((nei, 0))
                        queue.append((nei, dist + 1, 0))

            if last_color != 1:
                for nei in blue_adj[node]:
                    if (nei, 1) not in visited:
                        visited.add((nei, 1))
                        queue.append((nei, dist + 1, 1))

        return result



