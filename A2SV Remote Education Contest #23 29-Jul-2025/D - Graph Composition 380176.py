# Problem: D - Graph Composition - https://codeforces.com/gym/625306/problem/D

from collections import defaultdict
 
 
def dfs(node, adj, visited, component_id, comp_id):
    stack = [node]
    while stack:
        curr = stack.pop()
        if visited[curr]:
            continue
        visited[curr] = True
        component_id[curr] = comp_id
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                stack.append(neighbor)
 
t = int(input())
for _ in range(t):
    n, m1, m2 = map(int, input().split())
    
    F_adj = [[] for _ in range(n + 1)]
    G_adj = [[] for _ in range(n + 1)]
    F_edges = []
 
    for _ in range(m1):
        u, v = map(int, input().split())
        F_adj[u].append(v)
        F_adj[v].append(u)
        F_edges.append((u, v))
 
    for _ in range(m2):
        u, v = map(int, input().split())
        G_adj[u].append(v)
        G_adj[v].append(u)
 
    # Build G components
    g_component = [0] * (n + 1)
    visited = [False] * (n + 1)
    g_id = 1
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, G_adj, visited, g_component, g_id)
            g_id += 1
 
    # rmove edges in F that violate G connectivi
    remove_count = 0
    new_F_adj = [[] for _ in range(n + 1)]
    for u, v in F_edges:
        if g_component[u] != g_component[v]:
            remove_count += 1
        else:
            new_F_adj[u].append(v)
            new_F_adj[v].append(u)
 
    # build F components on filtered F graph
    f_component = [0] * (n + 1)
    visited = [False] * (n + 1)
    f_id = 1
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, new_F_adj, visited, f_component, f_id)
            f_id += 1
 
    g_to_f = defaultdict(set)
    for i in range(1, n + 1):
        g_to_f[g_component[i]].add(f_component[i])
 
    add_count = sum(len(s) - 1 for s in g_to_f.values())
    print(remove_count + add_count)