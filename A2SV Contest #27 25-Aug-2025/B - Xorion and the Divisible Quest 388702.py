# Problem: B - Xorion and the Divisible Quest - https://codeforces.com/gym/630556/problem/B

import math

n = int(input())
arr = list(map(int, input().split()))
g = arr[0]
for x in arr[1:]:
    g = math.gcd(g, x)
if g in arr:
    print(g)
else:
    print(-1)
