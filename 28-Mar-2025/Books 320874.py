# Problem: Books - https://codeforces.com/contest/279/problem/B

def max_books(n, t, books):
    left = 0
    total_time = 0
    max_books = 0
    
    for right in range(n):
        total_time += books[right]
        
        while total_time > t:
            total_time -= books[left]
            left += 1
            
        max_books = max(max_books, right - left + 1)
    
    print(max_books)

# Reading input
n, t = map(int, input().split())
books = list(map(int, input().split()))

# Solve the problem
max_books(n, t, books)