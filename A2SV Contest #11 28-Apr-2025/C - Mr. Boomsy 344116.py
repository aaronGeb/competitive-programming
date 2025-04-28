# Problem: C - Mr. Boomsy - https://codeforces.com/gym/605795/problem/C

t = int(input())
for _ in range(t):
    s = input().strip()
    st = []
    for c in s:
        if st and ((st[-1] == 'A' and c == 'B') or (st[-1] == 'B' and c == 'B')):
            st.pop()
        else:
            st.append(c)
    print(len(st))