# Problem: The Two Routes - https://codeforces.com/problemset/problem/601/A

from collections import deque
import sys


def bfs(n, adj_matrix, use_rail):
    dist = [-1] * n
    q = deque([0])
    dist[0] = 0
    while q:
        u = q.popleft()
        for v in range(n):
            if v == u:
                continue
            is_rail = adj_matrix[u][v]
            if use_rail and not is_rail:
                continue
            if (not use_rail) and is_rail:
                continue
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist


def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [[False] * n for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u][v] = True
        adj[v][u] = True
    dist_rail = bfs(n, adj, use_rail=True)

    dist_road = bfs(n, adj, use_rail=False)

    d1 = dist_rail[n - 1]
    d2 = dist_road[n - 1]
    if d1 == -1 or d2 == -1:
        print(-1)
    else:
        print(max(d1, d2))


if __name__ == "__main__":
    main()
