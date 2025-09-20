# Problem: B - Game of Mathletes - https://codeforces.com/gym/633600/problem/B

import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = [0] * (n + 1)
    for x in arr:
        if 1 <= x <= n:
            cnt[x] += 1

    score = 0
    for v in range(1, (k // 2) + 1):
        u = k - v
        if u < 1 or u > n:
            continue
        if u == v:
            continue
        if v < u:
            score += min(cnt[v], cnt[u])

    if k % 2 == 0:
        mid = k // 2
        if 1 <= mid <= n:
            score += cnt[mid] // 2

    print(score)
