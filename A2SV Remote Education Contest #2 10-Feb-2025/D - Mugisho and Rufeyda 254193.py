# Problem: D - Mugisho and Rufeyda - https://codeforces.com/gym/586622/problem/D

def find_number(n, t):
    # Calculate the smallest n-digit number
    min_num = 10 ** (n - 1)
    # Calculate the largest n-digit number
    max_num = 10 ** n - 1
    
    # Handle edge case: n = 1
    if n == 1:
        for num in range(1, 10):
            if num % t == 0:
                return num
        return -1
    
    # Handle edge case: t = 10
    if t == 10:
        if n < 2:
            return -1
        else:
            return min_num if min_num % t == 0 else min_num + (t - (min_num % t))
    
    # General case
    for num in range(min_num, max_num + 1):
        if num % t == 0:
            return num
    return -1

# Input
n, t = map(int, input().split())

# Output
result = find_number(n, t)
print(result)