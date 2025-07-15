# Problem: F - Choo-Choo Choose Wisely! - https://codeforces.com/gym/622136/problem/F

import heapq
import sys


def main():
    n, m, k = [int(i) for i in sys.stdin.readline().split()]
    graph = [[] for _ in range(n)]
    edges, train_edges = [], []
    inf = float('inf')

    for _ in range(m):
        u, v, w = [int(i) for i in sys.stdin.readline().split()]
        graph[u - 1].append((v - 1, w))
        graph[v - 1].append((u - 1, w))
        edges.append((u - 1, v - 1, w))

    for i in range(k):
        v, w = [int(i) for i in sys.stdin.readline().split()]
        graph[0].append((v - 1, w))
        graph[v - 1].append((0, w))
        edges.append((0, v - 1, w))
        train_edges.append((v - 1, w))

    d = [inf for _ in range(n)]
    d[0] = 0

    queue = []
    heapq.heappush(queue, (0, 0))

    while queue:
        r, v = heapq.heappop(queue)
        if d[v] == r:
            for u, w in graph[v]:
                if d[u] > r + w:
                    d[u] = r + w
                    heapq.heappush(queue, (d[u], u))

    new_graph = [0] * n

    for u, v, w in edges:
        if d[u] + w == d[v]:
            new_graph[v] += 1
        if d[v] + w == d[u]:
            new_graph[u] += 1

    ans = 0

    for i in range(k):
        v, w = train_edges[i]

        if d[v] < w:
            ans += 1

        if d[v] == w and new_graph[v] > 1:
            new_graph[v] -= 1
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()