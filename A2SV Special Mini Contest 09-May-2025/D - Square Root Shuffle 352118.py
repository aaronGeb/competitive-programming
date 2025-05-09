# Problem: D - Square Root Shuffle - https://codeforces.com/gym/608569/problem/D

import sys

def generate_sequence(n):
    if n == 2:
        return [1, 3]
    
    result = []
    mid = n // 2
    base = 4 * n

    for i in range(n):
        if n % 2 == 1:
            if i == 0:
                result.append(3 * n)
            elif i == mid:
                result.append(base)
            elif i == n - 1:
                result.append(5 * n)
            else:
                result.append(base - (mid - i))
        else:
            if i == 0:
                result.append(3 * n)
            elif i == n - 1:
                result.append(5 * n)
            elif i == mid - 1:
                result.append(base - 1)
            elif i == mid:
                result.append(base + 1)
            elif i < mid:
                result.append(base - (mid - i))
            else:
                result.append(base - (mid - 1 - i))
    
    return result

def solve():
    input_data = map(int, sys.stdin.read().split())
    it = iter(input_data)
    t = next(it)
    
    for _ in range(t):
        n = next(it)
        sequence = generate_sequence(n)
        print(' '.join(map(str, sequence)))

solve()