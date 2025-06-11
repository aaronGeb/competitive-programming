# Problem: Regular Graph - https://basecamp.eolymp.com/en/problems/5076

n, m = map(int, input().split())
degrees = [0] * (n + 1) 
for _ in range(m):
    u, v = map(int, input().split())
    degrees[u] += 1
    degrees[v] += 1
if len(set(degrees[1:])) == 1:
    print("YES")
else:
    print("NO")