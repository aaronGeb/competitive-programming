# Problem: F - Love Birds - https://codeforces.com/gym/613405/problem/F

import bisect

def solve():
    for _ in range(int(input())):
        while True:
            line = input().strip()
            if line:
                n, m = map(int, line.split())
                break

        flowers = [tuple(map(int, input().split())) for _ in range(m)]
        x_vals = sorted(x for x, _ in flowers)


        suffix_sum = [0] * (m + 1)
        for i in range(m - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + x_vals[i]

        max_total = 0
        for x, y in flowers:
            pos = bisect.bisect_right(x_vals, y)
            count = m - pos
            total = suffix_sum[pos]

            # Include current flower if its value fits
            if x <= y:
                total += x
                count += 1

            if count >= n:
                candidate = suffix_sum[m - n]
            else:
                candidate = total + (n - count) * y

            max_total = max(max_total, candidate)

        print(max_total)

solve()
