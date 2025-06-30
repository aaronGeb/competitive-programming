# Problem: B - New Year Transportation - https://codeforces.com/gym/618729/problem/B

n, t = map(int, input().split())
a = list(map(int, input().split()))

pos = 1
while pos < t:
    pos += a[pos - 1]

print("YES" if pos == t else "NO")