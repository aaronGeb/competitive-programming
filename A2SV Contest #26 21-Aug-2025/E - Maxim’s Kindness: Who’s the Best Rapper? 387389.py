# Problem: E - Maxim’s Kindness: Who’s the Best Rapper? - https://codeforces.com/gym/629689/problem/E

from collections import deque

def check(n, edges, k):
    graph = [[] for _ in range(n)]
    indegree = [0 for _ in range(n)] 
    for i in range(k):
        u, v = edges[i]
        graph[u].append(v)
        indegree[v] += 1

    queue = deque()
    dp = [0 for _ in range(n)]
    
    for node in range(n):
        if indegree[node] == 0:
            queue.append(node)
            dp[node] = 1
    
    battles = 0
    while queue:
        u = queue.popleft()
        battles += 1
        for v in graph[u]:
            if dp[v] < dp[u] + 1:
                dp[v] = dp[u] + 1
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    if battles < n:
        return False
    return max(dp) == n

def solve():
    n, m = list(map(int, input().split()))
    edges = []
    
    for _ in range(m):
        u, v = list(map(int, input().split()))
        edges.append((u -1, v - 1))
    
    #  Binary search on the value of k
    low = 0
    high = m
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if check(n, edges, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

print(solve())