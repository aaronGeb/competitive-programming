# Problem: H - Grid 1 - https://atcoder.jp/contests/dp/tasks/dp_h

MOD = 10**9 + 7

def count_paths(H, W, grid):
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    dp[1][1] = 1  

    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if i == 1 and j == 1:
                continue
            if grid[i-1][j-1] == '#':
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD

    return dp[H][W]

if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()
    H, W = map(int, data[:2])
    grid = []
    idx = 2
    for _ in range(H):
        grid.append(data[idx])
        idx += 1
    print(count_paths(H, W, grid))
