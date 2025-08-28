# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = UnionFind(len(edges))
        for u, v in edges:
            if not dsu.union(u, v):
                return [u, v]
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n+1))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  
        self.parent[py] = px
        return True