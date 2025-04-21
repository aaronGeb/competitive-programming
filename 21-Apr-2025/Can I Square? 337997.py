# Problem: Can I Square? - https://codeforces.com/contest/1915/problem/C

import math

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    root = int(math.isqrt(total))
    print("YES" if root * root == total else "NO")