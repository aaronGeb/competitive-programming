# Problem: G - Longest Path - https://atcoder.jp/contests/dp/tasks/dp_g

from collections import deque

def longest_path_in_dag(N, M, edges):
    adj = [[] for _ in range(N+1)]
    indeg = [0] * (N+1)

    # Build graph
    for u, v in edges:
        adj[u].append(v)
        indeg[v] += 1

    
    dp = [0] * (N+1)
    q = deque()
    for i in range(1, N+1):
        if indeg[i] == 0:
            q.append(i)

    while q:
        u = q.popleft()
        for v in adj[u]:
            dp[v] = max(dp[v], dp[u] + 1)
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    return max(dp)


if __name__ == "__main__":
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    print(longest_path_in_dag(N, M, edges))
