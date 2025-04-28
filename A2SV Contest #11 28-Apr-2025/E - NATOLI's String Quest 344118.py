# Problem: E - NATOLI's String Quest - https://codeforces.com/gym/605795/problem/E

s = input().strip()
t = []
u = []

st = [None] * len(s)
st[-1] = s[-1]
for i in range(len(s) - 2, -1, -1):
    st[i] = min(s[i], st[i + 1])

idx = 0
n = len(s)

while idx < n or t:
    if t and (idx == n or t[-1] <= st[idx]):
        u.append(t.pop())
    else:
        t.append(s[idx])
        idx += 1

print(''.join(u))