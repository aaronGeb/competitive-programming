# Problem: B - 01 Game - https://codeforces.com/gym/616066/problem/B

t = int(input())
for _ in range(t):
    s = input()
    cnt0 = s.count('0')
    cnt1 = s.count('1')
    moves = min(cnt0, cnt1)
    if moves % 2 == 1:
        print("DA")
    else:
        print("NET")