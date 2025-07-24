# Problem: Build a Matrix With Conditions - https://leetcode.com/problems/build-a-matrix-with-conditions/

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topoSort(conds: List[List[int]]) -> List[int]:
            graph = defaultdict(list)
            indegree = [0] * (k + 1)
            for u, v in conds:
                graph[u].append(v)
                indegree[v] += 1

            q = deque([node for node in range(1, k + 1) if indegree[node] == 0])
            order = []
            while q:
                u = q.popleft()
                order.append(u)
                for nei in graph[u]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)

            return order if len(order) == k else []

        rowOrder = topoSort(rowConditions)
        colOrder = topoSort(colConditions)
        if not rowOrder or not colOrder:
            return []

        pos_in_row = {num: i for i, num in enumerate(rowOrder)}
        pos_in_col = {num: i for i, num in enumerate(colOrder)}

        ans = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            r = pos_in_row[num]
            c = pos_in_col[num]
            ans[r][c] = num
        return ans