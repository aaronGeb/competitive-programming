# Problem: E - Knapsack 2 - https://atcoder.jp/contests/dp/tasks/dp_e

import sys

def knapsack(N, W, items):
    INF = 10**15
    max_value = sum(v for _, v in items)

    
    dp = [INF] * (max_value + 1)
    dp[0] = 0

    for w, v in items:
        for val in range(max_value, v-1, -1):
            if dp[val - v] + w < dp[val]:
                dp[val] = dp[val - v] + w

    
    ans = 0
    for val in range(max_value+1):
        if dp[val] <= W:
            ans = val
    return ans


if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    N, W = int(data[0]), int(data[1])
    items = [(int(data[i]), int(data[i+1])) for i in range(2, 2*N+2, 2)]
    print(knapsack(N, W, items))
