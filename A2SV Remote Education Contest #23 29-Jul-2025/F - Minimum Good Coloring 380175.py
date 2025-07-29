# Problem: F - Minimum Good Coloring - https://codeforces.com/gym/625306/problem/F

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
edges = []
 
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append((v, i))
    edges.append((u, v))
 
color = [0] * m
visited = [0] * n
need_two_colors = False
 
def dfs(u):
    global need_two_colors
    visited[u] = 1
    for v, idx in graph[u]:
        if visited[v] == 0:
            color[idx] = 1
            dfs(v)
        elif visited[v] == 1:
            color[idx] = 2
            need_two_colors = True
        else:
            color[idx] = 1
    visited[u] = 2
 
for i in range(n):
    if visited[i] == 0:
        dfs(i)
 
if need_two_colors:
    print(2)
else:
    print(1)
print(*color)