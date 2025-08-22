# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b

def frog():
  n, k = list(map(int, input().split()))
  h = list(map(int, input().split()))
  
  dp = [float("inf")] * n
  dp[0] = 0
  dp[1] = dp[0] + abs(h[1] - h[0])
  for i in range(2, n):
    for j in range(1, k + 1):
      if i - j < 0:
        break
      dp[i] = min (dp[i], dp[i - j] + abs(h[i] - h[i - j]))
      
  return dp[n - 1]
print(frog())