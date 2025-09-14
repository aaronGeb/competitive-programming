# Problem: Divisibility by 2^n - https://codeforces.com/contest/1744/problem/D

import sys

def v2(x):
    cnt = 0
    while x % 2 == 0:
        cnt += 1
        x //= 2
    return cnt

def solve_one(n, arr):
    total = sum(v2(x) for x in arr)
    if total >= n:
        return 0
    need = n - total
    contribs = [v2(i) for i in range(1, n+1)]
    contribs.sort(reverse=True)
    taken = 0
    acc = 0
    for c in contribs:
        if c == 0:
            continue
        acc += c
        taken += 1
        if acc >= need:
            return taken
    return -1

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    t = next(it)
    out_lines = []
    for _ in range(t):
        n = next(it)
        arr = [next(it) for _ in range(n)]
        out_lines.append(str(solve_one(n, arr)))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
