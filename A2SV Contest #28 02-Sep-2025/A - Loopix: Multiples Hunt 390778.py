# Problem: A - Loopix: Multiples Hunt - https://codeforces.com/gym/632067/problem/A

import sys

def solve():
    l, r, k = map(int, sys.stdin.readline().split())

    low = 0
    high = r - l + 1
    ans = 0

    while low <= high:
        m = low + (high - low) // 2

        if m == 0:
            low = m + 1
            continue
        last_num = l + m - 1
        if last_num <= r and (r // last_num) >= k:
            ans = m
            low = m + 1
        else:
            high = m - 1

    print(ans)


try:
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()
except (IOError, ValueError):
    pass
