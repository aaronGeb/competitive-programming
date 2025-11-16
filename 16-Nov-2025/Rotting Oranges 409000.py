# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    queue.append((r,c,0))
                elif grid[r][c] == 1:
                    fresh +=1
        if fresh==0:
            return 0
        direction = [(1,0), (-1,0), (0,-1),(0,1)]
        time = 0
        while queue:
            r, c, time = queue.popleft()
            for dr,dc in direction:
                nr,nc = dr+r, dc+c
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                    grid[nr][nc] = 2
                    fresh -=1
                    queue.append((nr,nc,time+1))
        return time if fresh==0 else -1