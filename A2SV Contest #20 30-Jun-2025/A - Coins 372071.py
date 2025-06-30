# Problem: A - Coins - https://codeforces.com/gym/618729/problem/A

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if n % 2 == 0:
        print("YES")
    else:
        if k % 2 == 1:
            print("YES")
        else:
            print("NO")
