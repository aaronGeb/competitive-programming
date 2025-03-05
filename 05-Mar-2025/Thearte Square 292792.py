# Problem: Thearte Square - https://codeforces.com/problemset/problem/1/A

def minimum_flagstones(n, m, a):
    num_flagstones_length = (n + a - 1) // a
    num_flagstones_width = (m + a - 1) // a
    return num_flagstones_length * num_flagstones_width
 
# Input: n, m, a
n, m, a = map(int, input().split())
print(minimum_flagstones(n, m, a))