# Problem: Odd Sum - https://codeforces.com/problemset/problem/797/B

import sys

def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    total_sum = 0
    smallest_positive_odd = float('inf')
    largest_negative_odd = float('-inf')

    for num in a:
        if num > 0:
            total_sum += num
            if num % 2 != 0:
                smallest_positive_odd = min(smallest_positive_odd, num)
        elif num < 0:
            if num % 2 != 0:
                largest_negative_odd = max(largest_negative_odd, num)

    if total_sum % 2 != 0:
        print(total_sum)
    else:
        if smallest_positive_odd == float('inf') and largest_negative_odd == float('-inf'):
            ans = float('-inf')
            for num in a:
                if num % 2 != 0:
                    ans = max(ans, num)
            print(ans)
        elif smallest_positive_odd == float('inf'):
            print(total_sum + largest_negative_odd)
        elif largest_negative_odd == float('-inf'):
            print(total_sum - smallest_positive_odd)
        else:
            if smallest_positive_odd <= abs(largest_negative_odd):
                print(total_sum - smallest_positive_odd)
            else:
                print(total_sum + largest_negative_odd)

solve()