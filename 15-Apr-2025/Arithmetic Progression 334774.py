# Problem: Arithmetic Progression - https://codeforces.com/problemset/problem/382/C

from collections import Counter
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    if n == 1:
        print(-1)
        return

    if n == 2:
        a, b = arr
        d = b - a
        res = set()
        res.add(a - d)
        res.add(b + d)
        if d % 2 == 0:
            res.add(a + d // 2)
        print(len(res))
        print(' '.join(map(str, sorted(res))))
        return

    # For n >= 3
    diffs = []
    for i in range(1, n):
        diffs.append(arr[i] - arr[i - 1])

    
    count = Counter(diffs)

    if len(count) > 2:
        print(0)
        return
    elif len(count) == 1:
        d = diffs[0]
        res = [arr[0] - d, arr[-1] + d]
        if res[0] == res[1]:
            print(1)
            print(res[0])
        else:
            print(2)
            print(' '.join(map(str, sorted(res))))
        return
    else:
        d1, d2 = sorted(count.keys())
        if count[d1] == 1 and d1 == 2 * d2:
            for i in range(1, n):
                if arr[i] - arr[i - 1] == d1:
                    print(1)
                    print(arr[i - 1] + d2)
                    return
        elif count[d2] == 1 and d2 == 2 * d1:
            for i in range(1, n):
                if arr[i] - arr[i - 1] == d2:
                    print(1)
                    print(arr[i - 1] + d1)
                    return
        else:
            print(0)
            return
if __name__ == "__main__":
   
    solve()