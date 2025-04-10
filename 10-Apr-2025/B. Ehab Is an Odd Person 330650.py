# Problem: B. Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

def process_array(arr):
    has_odd = any(x % 2 == 1 for x in arr)
    has_even = any(x % 2 == 0 for x in arr)

    if has_odd and has_even:
        arr.sort()
    
    print(*arr)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    process_array(arr)
