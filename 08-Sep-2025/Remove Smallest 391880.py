# Problem: Remove Smallest - https://codeforces.com/problemset/problem/1399/A

def can_reduce(t, test_cases):
    results = []

    for case in test_cases:
        n, a = case
        a.sort()
        possible = True
        for i in range(n - 1):
            if a[i + 1] - a[i] > 1:
                possible = False
                break
        results.append("YES" if possible else "NO")

    return results


import sys

input = sys.stdin.readline
t = int(input())
test_cases = [
    tuple(map(int, input().split())) + (list(map(int, input().split())),)
    for _ in range(t)
]
results = can_reduce(t, test_cases)
print("\n".join(results))
