# Problem: A - Xorion and the Peaks - https://codeforces.com/gym/630556/problem/A

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    max_peaks = (n - 1) // 2
    
    if k > max_peaks:
        print(-1)
        continue
    
    arr = list(range(1, n + 1))
    
    for i in range(1, k + 1):
        arr[2*i - 1], arr[2*i] = arr[2*i], arr[2*i - 1]
    
    print(" ".join(map(str, arr)))
