# Problem: D - Split the Difference! - https://codeforces.com/gym/622136/problem/D

n, k = map(int, input().split())
A = list(map(int, input().split()))
diff = []
for i in range(1, n):
    diff.append(A[i] - A[i - 1])
diff.sort(reverse=True)
ans = A[-1] - A[0]
ans -= sum(diff[: k - 1])
print(ans)
