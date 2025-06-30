# Problem: E - Hongcow Builds A Nation - https://codeforces.com/gym/618729/problem/E

def solve():
    import sys
    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    special = set(map(int, input().split()))

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n + 1)

    def dfs(start):
        stack = [start]
        visited[start] = True
        size = 0
        has_special = False
        while stack:
            node = stack.pop()
            size += 1
            if node in special:
                has_special = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)
        return size, has_special

    def combination(x):
        return x * (x - 1) // 2

    total_non_special = 0
    largest_special_size = 0
    special_sum = 0

    for i in range(1, n + 1):
        if not visited[i]:
            size, has_special = dfs(i)
            if has_special:
                special_sum += combination(size)
                largest_special_size = max(largest_special_size, size)
            else:
                total_non_special += size

    # Recalculate contribution of largest special component
    special_sum -= combination(largest_special_size)
    special_sum += combination(largest_special_size + total_non_special)

    result = special_sum - m
    print(result)

solve()