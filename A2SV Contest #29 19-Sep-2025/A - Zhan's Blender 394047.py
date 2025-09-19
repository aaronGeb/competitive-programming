# Problem: A - Zhan's Blender - https://codeforces.com/gym/633600/problem/A

import sys
input = sys.stdin.readline
 
def solve():
    t = int(input().strip())
    res = []
    for _ in range(t):
        n = int(input().strip())
        x, y = map(int, input().split())
        if n == 0:
            res.append("0")
            continue
        ans = max((n + x - 1) // x, (n + y - 1) // y)
        res.append(str(ans))
    print("\n".join(res))
 
 
solve()