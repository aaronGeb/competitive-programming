# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

def is_power_of_two(n):
    return (n & (n - 1)) == 0
 
t = int(input())
for _ in range(t):
    x = int(input())
    if x == 1:
        print(3)  
    elif x & 1:
        print(1)
    else:
       
        lsb = x & -x
        print(lsb if lsb != x else lsb + 1)