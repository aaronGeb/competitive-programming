# Problem: I - Coins - https://atcoder.jp/contests/dp/tasks/dp_i

N = int(input())
p = list(map(float, input().split()))

dp = [0.0] * (N + 1)
dp[0] = 1.0

for i in range(N):
    for k in range(i, -1, -1):
        dp[k + 1] += dp[k] * p[i]
        dp[k] *= (1 - p[i])

threshold = N // 2
result = sum(dp[threshold + 1:])
print(f"{result:.10f}")