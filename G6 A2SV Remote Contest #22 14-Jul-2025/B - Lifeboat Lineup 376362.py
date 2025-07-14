# Problem: B - Lifeboat Lineup - https://codeforces.com/gym/622136/problem/B

n = int(input())
r = []
wo__chi = []
men = []
cap = []
for _ in range(n):
    name, status = input().split()
    if status == "rat":
        r.append(name)
    elif status == "woman" or status == "child":
        wo__chi.append(name)
    elif status == "man":
        men.append(name)
    elif status == "captain":
        cap.append(name)

for name in r + wo__chi + men + cap:
    print(name)