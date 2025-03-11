# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

def merge_array(n, m, a, b):
    i, j = 0, 0
    result = []

    while i < n and j < m:
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    while i < n:
        result.append(a[i])
        i += 1

    while j < m:
        result.append(b[j])
        j += 1

    print(*result)


if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    merge_array(n, m, a, b)