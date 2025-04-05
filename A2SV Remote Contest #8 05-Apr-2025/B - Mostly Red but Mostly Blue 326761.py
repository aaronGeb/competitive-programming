# Problem: B - Mostly Red but Mostly Blue - https://codeforces.com/gym/599884/problem/B

import sys

def can_paint_sequence(n, arr):
    arr.sort()  
   
    red_sum = arr[-1]
    red_count = 1
    
    blue_sum = arr[0]
    blue_count = 1
    
    left = 1
    right = n - 2  
    
    while left <= right:
        blue_sum += arr[left]
        blue_count += 1
        left += 1
        
        if blue_count > red_count and blue_sum < red_sum:
            return "YES"
        
        red_sum += arr[right]
        red_count += 1
        right -= 1

    return "NO"

# Read input
t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().split()))
    print(can_paint_sequence(n, arr))