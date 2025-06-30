# Problem: C - The Lakes - https://codeforces.com/gym/618729/problem/C

import sys
#sys.setrecursionlimit(10**7)
input = sys.stdin.readline
 
 
def solve():
    t = int(input())
 
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
 
    for _ in range(t):
        n, m = map(int, input().split())
        grid = []
        for _ in range(n):
            grid.append(list(map(int, input().split())))
        visited = [[False] * m for _ in range(n)]
 
        def dfs(i, j):
            stack = [(i, j)]
            volume = 0
            visited[i][j] = True
 
            while stack:
                x, y = stack.pop()
                volume += grid[x][y]
 
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < n
                        and 0 <= ny < m
                        and not visited[nx][ny]
                        and grid[nx][ny] > 0
                    ):
                        visited[nx][ny] = True
                        stack.append((nx, ny))
            return volume
 
        max_volume = 0
 
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0 and not visited[i][j]:
                    lake_volume = dfs(i, j)
                    max_volume = max(max_volume, lake_volume)
 
        print(max_volume)
 
 
solve()