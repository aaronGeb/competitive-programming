# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C

def less_or_equal(n, k, arr):
    arr.sort()  
    if k == 0:
        return -1 if arr[0] == 1 else arr[0] - 1
    x = arr[k - 1]
    count = sum(1 for num in arr if num <= x)
    
    return x if count == k else -1

if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(less_or_equal(n, k, arr))