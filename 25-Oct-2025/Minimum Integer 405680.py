# Problem: Minimum Integer - https://codeforces.com/problemset/problem/1101/A

import sys

input_data = sys.stdin.read().strip().split()
q = int(input_data[0])
out_lines = []
idx = 1
for _ in range(q):
    l = int(input_data[idx]); r = int(input_data[idx+1]); d = int(input_data[idx+2])
    idx += 3
    if d < l:
        out_lines.append(str(d))
    else:
        k = r // d
        out_lines.append(str((k + 1) * d))

print("\n".join(out_lines))
