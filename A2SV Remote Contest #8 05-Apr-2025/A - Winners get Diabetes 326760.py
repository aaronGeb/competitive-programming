# Problem: A - Winners get Diabetes - https://codeforces.com/gym/599884/problem/A

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    seen = set()
    to = 0
    for p in s:
        if p not in seen:
            to += 2
            seen.add(p)
        else:
            to += 1
    print(to)