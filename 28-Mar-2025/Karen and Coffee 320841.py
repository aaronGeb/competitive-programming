# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

# Read input
n, k, q = map(int, input().split())

MAX_TEMP = 200000

freq = [0] * (MAX_TEMP + 2)  

for _ in range(n):
    li, ri = map(int, input().split())
    freq[li] += 1
    if ri + 1 <= MAX_TEMP:
        freq[ri + 1] -= 1

recommendations = [0] * (MAX_TEMP + 1)
recommendations[1] = freq[1]

for i in range(2, MAX_TEMP + 1):
    recommendations[i] = recommendations[i - 1] + freq[i]

admissible = [0] * (MAX_TEMP + 1)
for i in range(1, MAX_TEMP + 1):
    if recommendations[i] >= k:
        admissible[i] = 1
prefix_admissible = [0] * (MAX_TEMP + 1)
prefix_admissible[1] = admissible[1]

for i in range(2, MAX_TEMP + 1):
    prefix_admissible[i] = prefix_admissible[i - 1] + admissible[i]

for _ in range(q):
    a, b = map(int, input().split())
    if a > 1:
        print(prefix_admissible[b] - prefix_admissible[a - 1])
    else:
        print(prefix_admissible[b])