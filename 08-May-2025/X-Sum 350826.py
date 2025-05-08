# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(n)]

        diag1 = dict()  
        diag2 = dict()  

        for i in range(n):
            for j in range(m):
                diag1[i - j] = diag1.get(i - j, 0) + board[i][j]
                diag2[i + j] = diag2.get(i + j, 0) + board[i][j]

        max_sum = 0
        for i in range(n):
            for j in range(m):
                total = diag1[i - j] + diag2[i + j] - board[i][j]
                max_sum = max(max_sum, total)

        print(max_sum)

if __name__ == "__main__":
  solve()