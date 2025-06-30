# Problem: F - Non-academic Problem - https://codeforces.com/gym/618729/problem/F

import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        tin = [0] * (n + 1)
        low = [0] * (n + 1)
        visited = [False] * (n + 1)
        size = [1] * (n + 1)
        bridges = []

        timer = 1
        stack = []
        parent = [-1] * (n + 1)
        neighbors_idx = [0] * (n + 1)

        stack.append(1)
        visited[1] = True
        tin[1] = low[1] = timer
        timer += 1

        while stack:
            u = stack[-1]
            if neighbors_idx[u] < len(graph[u]):
                v = graph[u][neighbors_idx[u]]
                neighbors_idx[u] += 1

                if v == parent[u]:
                    continue

                if not visited[v]:
                    visited[v] = True
                    tin[v] = low[v] = timer
                    timer += 1
                    parent[v] = u
                    stack.append(v)
                else:
                    low[u] = min(low[u], tin[v])
            else:
                stack.pop()
                p = parent[u]
                if p != -1:
                    low[p] = min(low[p], low[u])
                    size[p] += size[u]
                    if low[u] > tin[p]:
                        # Found a bridge between p and u
                        bridges.append((p, u))

        total_pairs = n * (n - 1) // 2

        if not bridges:
            print(total_pairs)
            continue

        max_cut = 0
        for u, v in bridges:
            x = min(size[u], size[v])

            part1_after_cut = (n - x) * (n - x - 1) // 2
            part2_after_cut = x * (x - 1) // 2

            cut_value = total_pairs - (part1_after_cut + part2_after_cut)

            max_cut = max(max_cut, cut_value)

        print(total_pairs - max_cut)

solve()