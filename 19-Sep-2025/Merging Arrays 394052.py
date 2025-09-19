# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

def merge_sorted_arrays(a, b):
    n, m = len(a), len(b)
    i, j = 0, 0
    result = []
 
    # merge until one array is exhausted
    while i < n and j < m:
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
 
    # append leftovers
    if i < n:
        result.extend(a[i:])
    if j < m:
        result.extend(b[j:])
 
    return result
 
 
# Reading input and printing result
if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    merged = merge_sorted_arrays(a, b)
    print(*merged)