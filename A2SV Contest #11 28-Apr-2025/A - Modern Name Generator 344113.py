# Problem: A - Modern Name Generator - https://codeforces.com/gym/605795/problem/A

t = int(input())

for _ in range(t):
    cns = input().split()
    name = ''.join(s[0] for s in cns)
    print(name)