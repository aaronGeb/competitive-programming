# Problem: F - Luffy’s Lineup Challenge - https://codeforces.com/gym/594356/problem/F

n = int(input())
a = list(map(int,input().split()))
b = list(map(int, input().split()))
def next_index(start,target):
    for i in range(start,n):
        if b[i] == target:
            return i
swaps = []
for i in range(n):
    target = a[i]
    right = next_index(i,target)
 
    while right>i:
        swaps.append([right,right+1])
        b[right],b[right-1] = b[right-1],b[right]
        right-=1
count = 0
print(len(swaps))
for swap in swaps:
    print(*swap)