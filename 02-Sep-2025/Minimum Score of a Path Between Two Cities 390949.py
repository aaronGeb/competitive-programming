# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        for u, v, w in roads:
            g[u].append((v, w))
            g[v].append((u, w))

        seen = set([1])
        q = deque([1])
        ans = float('inf')

        while q:
            u = q.popleft()
            for v, w in g[u]:
                ans = min(ans, w)
                if v not in seen:
                    seen.add(v)
                    q.append(v)
        return ans