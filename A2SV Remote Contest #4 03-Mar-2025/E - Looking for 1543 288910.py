# Problem: E - Looking for 1543 - https://codeforces.com/gym/590201/problem/E

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    mat = []
    for i in range(n):
        mat.append(list(input()))
    count = 0
    for i in range (min((n//2),(m//2))):
        curr = []

        for j in range(i, m-i):
            curr.append(mat[i][j])

        for j in range(i+1, n-i-1):
            curr.append(mat[j][m-i-1])

        for j in range(m-i-1, i-1, -1):
            curr.append(mat[n-i-1][j])

        for j in range(n-i-2, i, -1):
            curr.append(mat[j][i])
        
        curr.extend(curr[:3])

        for j in range(len(curr)-3):
            if curr[j:j+4] == ['1','5','4','3']:
                count+=1

    print(count)