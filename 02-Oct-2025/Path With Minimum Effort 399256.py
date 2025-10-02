# Problem: Path With Minimum Effort - https://leetcode.com/problems/path-with-minimum-effort/description/

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        efforts = [[float('inf')] * n for _ in range(m)]
        efforts[0][0] = 0
        pq = [(0, 0, 0)]

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while pq:
            effort, x, y = heapq.heappop(pq)
            if (x, y) == (m-1, n-1):
                return effort
            if effort > efforts[x][y]:
                continue
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    diff = abs(heights[nx][ny] - heights[x][y])
                    new_effort = max(effort, diff)
                    if new_effort < efforts[nx][ny]:
                        efforts[nx][ny] = new_effort
                        heapq.heappush(pq, (new_effort, nx, ny))
        return -1
