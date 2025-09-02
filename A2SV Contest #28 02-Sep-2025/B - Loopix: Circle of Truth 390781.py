# Problem: B - Loopix: Circle of Truth - https://codeforces.com/gym/632067/problem/B

def solve():
    s = input()
    n_count = s.count('N')
    if n_count == 1:
        print("NO")
    else:
        print("YES")
t = int(input())
for _ in range(t):
    solve()