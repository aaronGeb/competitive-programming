# Problem: B - Too Hot to Code! - https://codeforces.com/gym/617023/problem/B

def min_rounds(t, test_cases):
    results = []

    for n, k, arr in test_cases:
        arr.sort()
        max_len = 1
        l = 0

        for r in range(1, n):
            if arr[r] - arr[r - 1] <= k:
                continue
            else:
                max_len = max(max_len, r - l)
                l = r
        
        max_len = max(max_len, n - l)  
        results.append(n - max_len)
    
    return results


t = int(input())
test_cases = []

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    test_cases.append((n, k, arr))

results = min_rounds(t, test_cases)
for res in results:
    print(res)