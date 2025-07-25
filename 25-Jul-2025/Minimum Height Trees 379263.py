# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <=2:
            return list(range(n))
        # build the graph
        graph = defaultdict(set)
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        # bfs
        leavel = deque([ k  for k in range(n) if len(graph[k])==1])
        nodes = n
        while nodes > 2:
            count = len(leavel)
            nodes -= count
            for _ in range(count):
                leaf = leavel.popleft()
                neigh = graph[leaf].pop()
                graph[neigh].remove(leaf)
                if len(graph[neigh]) == 1:
                    leavel.append(neigh)
        return list(leavel)
