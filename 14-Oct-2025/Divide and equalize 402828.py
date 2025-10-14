# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D

import math
from collections import defaultdict

def prime_factors(n):
    factors = defaultdict(int)
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] += 1
            n //= d
        d += 1
    if n > 1:
        factors[n] += 1
    return factors

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    total = defaultdict(int)

    for a in arr:
        for p, e in prime_factors(a).items():
            total[p] += e

    ok = all(v % n == 0 for v in total.values())
    print("YES" if ok else "NO")
