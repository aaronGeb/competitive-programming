# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        print(0)
        return

    n = data[0]
    s = data[1]
    a = data[2:]
    l = 0
    curr_sum = 0
    max_len = 0

    for r in range(n):
        curr_sum += a[r]
        while curr_sum > s and l <= r:
            curr_sum -= a[l]
            l += 1
        max_len = max(max_len, r - l + 1)

    print(max_len)

if __name__ == "__main__":
    main()
