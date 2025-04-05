# Problem: E - Keep the order - https://codeforces.com/gym/599884/problem/E

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
p = {tp: idx for idx, tp in enumerate(b)}

count = 0
max_p = -1

for trp in a:
    cp = p[trp]
    if cp < max_p:
        count += 1
    else:
        max_p = cp

print(count)