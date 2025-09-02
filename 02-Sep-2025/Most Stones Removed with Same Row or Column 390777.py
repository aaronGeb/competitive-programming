# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        if n == 0:
            return 0
        rows = defaultdict(list)
        cols = defaultdict(list)
        for i, (r, c) in enumerate(stones):
            rows[r].append(i)
            cols[c].append(i)

        visited = [False] * n
        components = 0

        for i in range(n):
            if visited[i]:
                continue
           
            components += 1
            dq = deque([i])
            visited[i] = True
            while dq:
                u = dq.popleft()
                r, c = stones[u]
               
                for v in rows[r]:
                    if not visited[v]:
                        visited[v] = True
                        dq.append(v)
               
                for v in cols[c]:
                    if not visited[v]:
                        visited[v] = True
                        dq.append(v)
               
                rows[r].clear()
                cols[c].clear()

        return n - components
   