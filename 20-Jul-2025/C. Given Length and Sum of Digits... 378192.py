# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

m, s = map(int, input().split())
 
def find_min(m, s):
    if s == 0:
        return "0" if m == 1 else "-1"
    res = [0] * m
    res[0] = 1
    remaining = s - 1
    for i in range(m - 1, 0, -1):
        if remaining >= 9:
            res[i] = 9
            remaining -= 9
        else:
            res[i] = remaining
            remaining = 0
    if remaining > 0:
        res[0] += remaining
    if res[0] > 9:
        return "-1"
    return ''.join(map(str, res))
 
def find_max(m, s):
    if s == 0:
        return "0" if m == 1 else "-1"
    res = [0] * m
    remaining = s
    for i in range(m):
        if remaining >= 9:
            res[i] = 9
            remaining -= 9
        else:
            res[i] = remaining
            remaining = 0
    if remaining > 0:
        return "-1"
    return ''.join(map(str, res))
 
if s == 0:
    if m == 1:
        print("0 0")
    else:
        print("-1 -1")
else:
    if s < 1 or s > 9 * m:
        print("-1 -1")
    else:
        min_num = find_min(m, s)
        max_num = find_max(m, s)
        if min_num == "-1" or max_num == "-1":
            print("-1 -1")
        else:
            print(min_num, max_num)