# Problem: Good Subarrays (Easy Version) - https://codeforces.com/problemset/problem/1736/C1

import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    mn = float("inf")
    ans = 0

    for i in range(n):
        c = a[i] - (i + 1)
        mn = min(mn, c)
        l_min = max(1, 1 - mn)

        ans += (i + 1) - l_min + 1

    print(ans)
