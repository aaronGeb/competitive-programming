# Problem: B - Aaron and Repeated Letters - https://codeforces.com/gym/605795/problem/B

s = input().strip()
st = []

for c in s:
    if st and st[-1] == c:
        st.pop()  
    else:
        st.append(c) 

print(''.join(st))