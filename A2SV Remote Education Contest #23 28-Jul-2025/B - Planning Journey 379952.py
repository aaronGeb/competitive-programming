# Problem: B - Planning Journey - https://codeforces.com/gym/625306/problem/B

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    cnt = 0
    i = 0
    ones = sum(a[:k])

    while i <= n - k:
        if ones == 0:
            cnt += 1
            i += k + 1
            if i <= n - k:
                ones = sum(a[i:i + k])
        else:
          
            if a[i] == 1:
                ones -= 1
            if i + k < n and a[i + k] == 1:
                ones += 1
            i += 1

    print(cnt)
