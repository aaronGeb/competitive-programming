# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

def insertionSort1(n, arr):
    val = arr[-1]
    for i in range(n - 2, -2, -1):
        if i >= 0 and arr[i] > val:
            arr[i + 1] = arr[i]
        else:
            arr[i + 1] = val
        print(*arr)
        if i >= 0 and arr[i] <= val:
            break
