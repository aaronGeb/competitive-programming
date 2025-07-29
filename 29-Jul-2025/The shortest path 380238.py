# Problem: The shortest path - https://basecamp.eolymp.com/en/problems/4853

from collections import deque, defaultdict
import sys
input = sys.stdin.read

def solve():
    data = input().split()
    idx = 0

    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    a = int(data[idx]) - 1; idx += 1
    b = int(data[idx]) - 1; idx += 1

    graph = [[] for _ in range(n)]
    for _ in range(m):
        u = int(data[idx]) - 1; idx += 1
        v = int(data[idx]) - 1; idx += 1
        graph[u].append(v)
        graph[v].append(u)

    # BFS
    dist = [-1] * n
    parent = [-1] * n
    queue = deque()
    queue.append(a)
    dist[a] = 0

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[current] + 1
                parent[neighbor] = current
                queue.append(neighbor)

    if dist[b] == -1:
        print(-1)
    else:
        print(dist[b])
        path = []
        cur = b
        while cur != -1:
            path.append(cur + 1) 
            cur = parent[cur]
        print(' '.join(map(str, reversed(path))))
solve()
