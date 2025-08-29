# Problem: D - Xorion on the Number Line - https://codeforces.com/gym/630556/problem/D

test = int(input())
for _ in range(test):
    n, k, q = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    brr = [0] + list(map(int, input().split()))

    for _ in range(q):
        dist = int(input())
        
        
        low, high = 0, k
        pos = 0
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] <= dist:
                pos = mid
                low = mid + 1
            else:
                high = mid - 1

        # Calculate time
        if arr[pos] == dist:
            print(brr[pos], end=" ")
        else:
            time = brr[pos] + (dist - arr[pos]) * (brr[pos+1] - brr[pos]) // (arr[pos+1] - arr[pos])
            print(time, end=" ")

    print()