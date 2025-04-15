# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

from collections import defaultdict

def count_pairs(t, test_cases):
    results = []

    for n, a in test_cases:
        freq = defaultdict(int)
        for i in range(n):
            key = a[i] - i
            freq[key] += 1

        count = 0
        for val in freq.values():
            count += val * (val - 1) // 2

        results.append(count)

    return results


t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

for res in count_pairs(t, test_cases):
    print(res)