# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

# Read the 5x5 matrix
matrix = []
for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)
    for j in range(5):
        if row[j] == 1:
            x, y = i, j  # Position of '1'

# Calculate Manhattan distance to center (2, 2)
moves = abs(x - 2) + abs(y - 2)
print(moves)
