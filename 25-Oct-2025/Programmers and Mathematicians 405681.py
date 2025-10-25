# Problem: Programmers and Mathematicians - https://codeforces.com/problemset/problem/1611/B

import sys

data = list(map(int, sys.stdin.read().strip().split()))
t = data[0]
out = []
idx = 1
for _ in range(t):
    a = data[idx]; b = data[idx+1]; idx += 2
    out.append(str(min((a + b) // 4, a, b)))
print("\n".join(out))
