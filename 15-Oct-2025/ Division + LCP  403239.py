# Problem:  Division + LCP  - https://codeforces.com/contest/1968/problem/G1

import sys
from bisect import bisect_left

input = sys.stdin.readline

MOD1 = 10**9+7
MOD2 = 10**9+9
BASE = 91138233

def build_hashes(s):
    n = len(s)
    h1 = [0]*(n+1)
    h2 = [0]*(n+1)
    p1 = [1]*(n+1)
    p2 = [1]*(n+1)
    for i,ch in enumerate(s):
        v = ord(ch)
        h1[i+1] = (h1[i]*BASE + v) % MOD1
        h2[i+1] = (h2[i]*BASE + v) % MOD2
        p1[i+1] = (p1[i]*BASE) % MOD1
        p2[i+1] = (p2[i]*BASE) % MOD2
    return (h1,h2,p1,p2)

def get_hash(h1,h2,p1,p2,l,r):
    x1 = (h1[r] - h1[l]*p1[r-l]) % MOD1
    x2 = (h2[r] - h2[l]*p2[r-l]) % MOD2
    return (x1,x2)

def max_k_for_L(s, k, L, hashes):
    n = len(s)
    if L == 0:
        return k <= n
    if L > n:
        return False
    h1,h2,p1,p2 = hashes
    prefix_hash = get_hash(h1,h2,p1,p2,0,L)
    pos = []
  
    for i in range(0, n - L + 1):
        if get_hash(h1,h2,p1,p2,i,i+L) == prefix_hash:
            pos.append(i)
    if not pos or pos[0] != 0:
        if 0 not in pos:
            return False
    cur = 0
    count = 1
    last_index = 0
    while True:
        need = cur + L
        j = bisect_left(pos, need)
        if j >= len(pos):
            last_index = cur
            break
        cur = pos[j]
        count += 1
        last_index = cur
        if count >= k:
            if n - cur >= L:
                return True
            else:
                continue
    if n - last_index < L:
        return False
    return count >= k

def solve():
    t = int(input().strip())
    out_lines = []
    for _ in range(t):
        n,l,r = map(int, input().split())
        k = l
        s = input().strip()
        hashes = build_hashes(s)
        lo = 0
        hi = n
        ans = 0
        while lo <= hi:
            mid = (lo + hi)//2
            if max_k_for_L(s, k, mid, hashes):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        out_lines.append(str(ans))
    print("\n".join(out_lines))

if __name__ == "__main__":
    solve()
