# Problem: C - Sort - https://codeforces.com/gym/625306/problem/C

t = int(input())
for _ in range(t):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    
    costs = [a[i] + i + 1 for i in range(n)] 
    costs.sort()
    
    used = 0
    for cost in costs:
        if c >= cost:
            c -= cost
            used += 1
        else:
            break
    print(used)
