# Problem: Team - https://codeforces.com/contest/231/problem/A

def team(n):
    count = 0
    for _ in range(n):
        a, b, c = map(int, input().split())
        if a + b + c >= 2:
            count += 1
    return count


# read the input
if __name__ == "__main__":
  n = int(input())
  print(team(n))