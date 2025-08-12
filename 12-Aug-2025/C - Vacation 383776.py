# Problem: C - Vacation - https://atcoder.jp/contests/dp/tasks/dp_c

import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    it = iter(data)
    N = next(it)

    a = next(it); b = next(it); c = next(it)
    prev0, prev1, prev2 = a, b, c

    for _ in range(1, N):
        a = next(it); b = next(it); c = next(it)
        cur0 = a + max(prev1, prev2)
        cur1 = b + max(prev0, prev2)
        cur2 = c + max(prev0, prev1)
        prev0, prev1, prev2 = cur0, cur1, cur2

    print(max(prev0, prev1, prev2))

if __name__ == "__main__":
    main()
