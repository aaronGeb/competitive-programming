# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D

import sys
import math

def prime_factors(x):
    factors = {}
    if x == 1:
        return factors
    # Handle 2 separately
    while x % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        x = x // 2
    # Check odd divisors up to sqrt(x)
    i = 3
    max_factor = math.sqrt(x) + 1
    while i <= max_factor:
        while x % i == 0:
            factors[i] = factors.get(i, 0) + 1
            x = x // i
            max_factor = math.sqrt(x) + 1
        i += 2
    if x > 1:
        factors[x] = factors.get(x, 0) + 1
    return factors

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
        
        total_factors = {}
        for num in a:
            if num == 1:
                continue
            factors = prime_factors(num)
            for p, cnt in factors.items():
                total_factors[p] = total_factors.get(p, 0) + cnt
        
        possible = True
        for p, cnt in total_factors.items():
            if cnt % n != 0:
                possible = False
                break
        
        print("YES" if possible else "NO")

solve()