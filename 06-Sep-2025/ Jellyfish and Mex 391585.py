# Problem:  Jellyfish and Mex - https://codeforces.com/problemset/problem/1875/D

import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    it = iter(input_data)
    t = int(next(it))
    out_lines = []
    INF = 10**30

    for _ in range(t):
        n = int(next(it))
        cnt = [0] * (n + 1)   
        for _ in range(n):
            x = int(next(it))
            if 0 <= x <= n:
                cnt[x] += 1

        
        m = 0
        while m <= n and cnt[m] > 0:
            m += 1

        
        dp = [INF] * (n + 1)
        dp[m] = 0

        
        for i in range(m, 0, -1):
            base = dp[i]
            if base >= INF:
                continue
            
            for j in range(i):
                val = base + i * cnt[j]
                if val < dp[j]:
                    dp[j] = val

       
        ans = dp[0] - m
        out_lines.append(str(ans))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()
