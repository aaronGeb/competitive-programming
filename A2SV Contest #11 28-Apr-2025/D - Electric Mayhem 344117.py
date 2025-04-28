# Problem: D - Electric Mayhem - https://codeforces.com/gym/605795/problem/D

s = input()
st = []
for i in range(len(s)):
    if st and s[i] == st[-1]:
        st.pop()
    else:
        st.append(s[i])
if st:
    print("No")
else:
    print("Yes")