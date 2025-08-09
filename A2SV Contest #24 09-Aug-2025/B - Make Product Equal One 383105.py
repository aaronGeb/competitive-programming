# Problem: B - Make Product Equal One - https://codeforces.com/gym/626626/problem/B

n = int(input())
a = list(map(int, input().split()))
cost = 0
neg = 0
z = 0
for i in a:
    if i == 0:
        cost += 1
        z += 1
    elif i > 0:
        cost += i - 1
    else:
        cost += -1 - i
        neg += 1
if neg % 2 == 1 and z == 0:
    cost += 2
print(cost)