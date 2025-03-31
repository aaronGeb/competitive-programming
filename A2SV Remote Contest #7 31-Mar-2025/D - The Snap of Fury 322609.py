# Problem: D - The Snap of Fury - https://codeforces.com/gym/596004/problem/D

import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    L = list(map(int, input[ptr:ptr + n]))
    ptr += n

    # Initialize a difference array with size n + 2
    diff = [0] * (n + 2)

    for k in range(1, n + 1):
        L_k = L[k - 1]
        start = max(1, k - L_k)
        end = k - 1
        if start <= end:
            diff[start] += 1
            if end + 1 <= n:
                diff[end + 1] -= 1

    # Compute the prefix sum to find the killed warriors
    killed = 0
    survivors = 0
    for i in range(1, n + 1):
        killed += diff[i]
        if killed == 0:
            survivors += 1

    print(survivors)

solve()