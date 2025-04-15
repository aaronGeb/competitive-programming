# Problem: B - Ski Resort - https://codeforces.com/gym/603156/problem/B

def count_vacation_ways(test_cases):
    results = []
    for n, k, q, a in test_cases:
        count = 0
        length = 0
        for temp in a:
            if temp <= q:
                length += 1
            else:
                if length >= k:
                    ways = (length - k + 1) * (length - k + 2) // 2
                    count += ways
                length = 0
        if length >= k:
            ways = (length - k + 1) * (length - k + 2) // 2
            count += ways
        results.append(count)
    return results


t = int(input())
test_cases = []
for _ in range(t):
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    test_cases.append((n, k, q, a))

# Output
for res in count_vacation_ways(test_cases):
    print(res)