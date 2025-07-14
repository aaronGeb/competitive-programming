# Problem: C - The Double-Holed Culprit - https://codeforces.com/gym/622136/problem/C

n = int(input())
p = list(map(int, input().split()))
for s in range(1, n + 1):
    visited = set()
    curr = s
    while curr not in visited:
        visited.add(curr)
        curr = p[curr - 1]
    print(curr, end=' ')