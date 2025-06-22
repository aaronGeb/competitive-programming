# Problem: Cities and Roads - https://www.eolymp.com/en/contests/9060/problems/78597

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

road_count = 0
for i in range(n):
    for j in range(i + 1, n):
        if matrix[i][j] == 1:
            road_count += 1

print(road_count)