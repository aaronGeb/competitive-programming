# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

def max_alternating_sum(t, test_cases):
    results = []
    for n, a in test_cases:
        total = 0
        i = 0
        while i < n:
            current_max = a[i]
            sign = a[i] > 0
            i += 1
            while i < n and (a[i] > 0) == sign:
                current_max = max(current_max, a[i])
                i += 1
            total += current_max
        results.append(total)
    return results
 
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))
 
results = max_alternating_sum(t, test_cases)
for res in results:
    print(res)