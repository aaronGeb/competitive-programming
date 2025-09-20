# Problem: C - Binary Deque - https://codeforces.com/gym/633600/problem/C

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))

    l = 0
    cur = 0
    best = -1  

    for r in range(n):
        cur += arr[r]
        
        while l <= r and cur > s:
            cur -= arr[l]
            l += 1
        if cur == s:
            best = max(best, r - l + 1)

    if best == -1:
        if s == 0:
            
            print(n)
        else:
            print(-1)
    else:
        print(n - best)
