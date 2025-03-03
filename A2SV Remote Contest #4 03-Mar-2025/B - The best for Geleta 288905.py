# Problem: B - The best for Geleta - https://codeforces.com/gym/590201/problem/B

import sys 
input = sys.stdin.readline 

def solve():
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    result, curr_max = [0] * m, max(nums) 

    for i in range(m):
        op, l, r = map(str, input().split())
        if int(l) <= curr_max <= int(r):
            if op == '+':
                curr_max += 1
                result[i] = curr_max
            else:
                curr_max -= 1
                result[i] = curr_max
            
            continue
        
        result[i] = curr_max

    print(*result)

if __name__ == '__main__':
    for _ in range(int(input())):
        solve()