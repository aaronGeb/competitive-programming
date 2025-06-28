# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1 / value

        def dfs(x, y, visited):
            if x not in graph or y not in graph:
                return -1.0
            if y in graph[x]:
                return graph[x][y]
            visited.add(x)
            for nei in graph[x]:
                if nei not in visited:
                    temp = dfs(nei, y, visited)
                    if temp != -1.0:
                        return graph[x][nei] * temp
            return -1.0
        results = []
        for a, b in queries:
            results.append(dfs(a, b, set()))
        return results