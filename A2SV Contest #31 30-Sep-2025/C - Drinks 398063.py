# Problem: C - Drinks - https://codeforces.com/gym/637748/problem/C

n = int(input())
p = list(map(int, input().split()))
print(f'{sum(p) / n:.12f}')
