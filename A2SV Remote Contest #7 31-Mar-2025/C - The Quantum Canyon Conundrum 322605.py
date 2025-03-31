# Problem: C - The Quantum Canyon Conundrum - https://codeforces.com/gym/596004/problem/C

import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        a = list(map(int, input[ptr:ptr + n]))
        ptr += n
        
        valid_segments = 0
        i = 0
        while i < n:
            l = i
            # Find the end of the current segment
            while i < n and a[i] == a[l]:
                i += 1
            r = i - 1
            # Check boundary conditions
            left_ok = (l == 0) or (a[l - 1] > a[l])
            right_ok = (r == n - 1) or (a[r] < a[r + 1])
            if left_ok and right_ok:
                valid_segments += 1
        print("YES" if valid_segments == 1 else "NO")

solve()