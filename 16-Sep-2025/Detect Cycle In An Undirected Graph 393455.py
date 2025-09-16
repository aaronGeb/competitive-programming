# Problem: Detect Cycle In An Undirected Graph - https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

class Solution:
	def isCycle(self, V, edges):
		from collections import defaultdict
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)  
        
        visited = [False] * V
        
        def dfs(node, parent):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    if dfs(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True
            return False
        for i in range(V):
            if not visited[i]:
                if dfs(i, -1):
                    return True
        return False