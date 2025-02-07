# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

from collections import defaultdict

def same_differences(t, test_cases):
    results = []

    for case in test_cases:
        n, a = case
        diff_count = defaultdict(int)
        total_pairs = 0

        for i in range(n):
            diff = a[i] - (i + 1)
            total_pairs += diff_count[diff]
            diff_count[diff] += 1

        results.append(total_pairs)

    return results


# Input reading
if __name__ == "__main__":
    t = int(input())  
    test_cases = []
    for _ in range(t):
        n = int(input()) 
        a = list(map(int, input().split()))  
        test_cases.append((n, a))

    results = same_differences(t, test_cases)

    # Output the results for all test cases
    for result in results:
        print(result)
