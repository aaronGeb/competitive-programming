# Problem: A - In Search of an Easy Problem - https://codeforces.com/gym/637748/problem/A

import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit()
n = int(data[0])
arr = data[1 : n + 1]
if "1" in arr:
    print("HARD")
else:
    print("EASY")
