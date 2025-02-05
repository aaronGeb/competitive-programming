# Problem: Presents - https://codeforces.com/problemset/problem/136/A

n = int(input())  
p = list(map(int, input().split()))  #

givers = [0] * n  

for i in range(n):
    givers[p[i] - 1] = i + 1 

print(" ".join(map(str, givers))) 