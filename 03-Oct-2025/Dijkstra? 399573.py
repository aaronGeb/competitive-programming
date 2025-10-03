# Problem: Dijkstra? - https://codeforces.com/problemset/problem/20/C

import sys
import heapq

def shortest_path(n, m, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    dist = [float("inf")] * (n + 1)
    parent = [-1] * (n + 1)
    dist[1] = 0
    pq = [(0, 1)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))

    if dist[n] == float("inf"):
        return [-1]

    path = []
    curr = n
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    path.reverse()

    return path


if __name__ == "__main__":
    data = sys.stdin.read().strip().split()
    n, m = map(int, data[:2])
    edges = []
    idx = 2
    for _ in range(m):
        u, v, w = map(int, data[idx : idx + 3])
        edges.append((u, v, w))
        idx += 3

    path = shortest_path(n, m, edges)
    print(" ".join(map(str, path)))
