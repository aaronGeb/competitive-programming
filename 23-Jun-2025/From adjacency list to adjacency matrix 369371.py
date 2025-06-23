# Problem: From adjacency list to adjacency matrix - https://basecamp.eolymp.com/en/problems/3982

n = int(input())
adj_matrix = [[0] * n for _ in range(n)]

for i in range(n):
    data = list(map(int, input().split()))
    count = data[0]
    for j in range(1, count + 1):
        to_vertex = data[j] - 1
        adj_matrix[i][to_vertex] = 1

for row in adj_matrix:
    print(*row)