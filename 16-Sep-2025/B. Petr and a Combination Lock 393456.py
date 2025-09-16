# Problem: B. Petr and a Combination Lock - https://codeforces.com/contest/1097/problem/B

import sys

def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    n = data[0]
    a = data[1:]
    for mask in range(1 << n):
        total = 0
        for i in range(n):
            if (mask >> i) & 1:
                total += a[i]
            else:
                total -= a[i]
        if total % 360 == 0:
            print("YES")
            return
    print("NO")

if __name__ == "__main__":
    main()
