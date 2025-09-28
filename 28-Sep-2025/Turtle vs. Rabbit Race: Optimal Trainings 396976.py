# Problem: Turtle vs. Rabbit Race: Optimal Trainings - https://codeforces.com/contest/1933/problem/E

import sys
import bisect

input = sys.stdin.readline

def value_increase(S, u):
    return S * (u + 1) - (S * (S + 1) // 2)

t = int(input().strip())
out_lines = []

for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().split()))
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + a[i - 1]

    q = int(input().strip())
    for _q in range(q):
        l, u = map(int, input().split())
        need = prefix[l - 1] + u
        r1 = bisect.bisect_left(prefix, need, lo=l, hi=n+1)

        best_r = None
        best_val = -10**30

        if r1 <= n:
            S1 = prefix[r1] - prefix[l - 1]
            v1 = value_increase(S1, u)
            best_r = r1
            best_val = v1

        r0 = r1 - 1
        if r0 >= l:
            S0 = prefix[r0] - prefix[l - 1]
            v0 = value_increase(S0, u)
            if v0 > best_val or (v0 == best_val and (best_r is None or r0 < best_r)):
                best_r = r0
                best_val = v0

        if best_r is None:
            best_r = n

        out_lines.append(str(best_r))

print("\n".join(out_lines))
