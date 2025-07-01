# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(queue, fresh_count):
            minutes = 0

            while queue and fresh_count > 0:
                for _ in range(len(queue)):
                    r, c = queue.popleft()

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fresh_count -= 1
                            queue.append((nr, nc))

                minutes += 1

            return minutes if fresh_count == 0 else -1

        queue = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        return bfs(queue, fresh)
