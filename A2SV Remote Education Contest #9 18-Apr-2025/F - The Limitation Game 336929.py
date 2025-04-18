# Problem: F - The Limitation Game - https://codeforces.com/gym/603156/problem/F

def main():
    n, k = map(int, input().split())
    a = input().strip()
    b = input().strip()

    ans = 0
    tag = 1

    for i in range(n):
        tag = tag * 2 - (1 if a[i] == 'b' else 0) - (1 if b[i] == 'a' else 0)
        tag = min(tag, k + 1)
        ans += min(tag, k)

    print(ans)

main()