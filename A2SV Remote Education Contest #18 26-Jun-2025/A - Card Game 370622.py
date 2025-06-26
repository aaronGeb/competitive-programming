# Problem: A - Card Game - https://codeforces.com/gym/616066/problem/A

t = int(input())
for _ in range(t):
    n, k1, k2 = map(int, input().split())
    player1 = list(map(int, input().split()))
    player2 = list(map(int, input().split()))

    if max(player1) > max(player2):
        print("YES")
    else:
        print("NO")