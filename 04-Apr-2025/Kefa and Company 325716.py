# Problem: Kefa and Company - https://codeforces.com/problemset/problem/580/B

def factor(n, d, fr):

    fr.sort()

    mf = 0
    cf = 0
    left = 0  

    for right in range(n):
        cf += fr[right][1]  
        while fr[right][0] - fr[left][0] >= d:
            cf -= fr[left][1]  
            left += 1
        mf = max(mf, cf)

    return mf

# Read input
n, d = map(int, input().split())
fr = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(factor(n, d, fr))