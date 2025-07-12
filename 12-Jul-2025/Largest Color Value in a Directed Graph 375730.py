# Problem: Largest Color Value in a Directed Graph - https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        dp = [[0] * 26 for _ in range(n)]
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
            dp[i][ord(colors[i]) - ord('a')] = 1

        visited = 0
        ans = 0

        while q:
            node = q.popleft()
            visited += 1
            ans = max(ans, max(dp[node]))
            for nei in graph[node]:
                for c in range(26):
                    dp[nei][c] = max(dp[nei][c], dp[node][c] + (1 if ord(colors[nei]) - ord('a') == c else 0))
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return ans if visited == n else -1