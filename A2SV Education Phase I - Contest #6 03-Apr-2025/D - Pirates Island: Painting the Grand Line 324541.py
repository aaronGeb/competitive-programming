# Problem: D - Pirates Island: Painting the Grand Line - https://codeforces.com/gym/594356/problem/D

import sys 
input = sys.stdin.readline 

def solve():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for i in range(n)]
    has_color = [0] * (n * m + 1)
    adj_found= [0] * (n * m + 1)

    for i in range(n):
        for j in range(m):
            has_color[grid[i][j]] = 1

            if i + 1 < n and grid[i][j] == grid[i + 1][j]:
                adj_found[grid[i][j]] = 1
            if j + 1 < m and grid[i][j] == grid[i][j + 1]:
                adj_found[grid[i][j]] = 1

    print(sum(has_color) + sum(adj_found) - 1 - max(adj_found))

if __name__ == '__main__':
    for _ in range(int(input())):
        solve()