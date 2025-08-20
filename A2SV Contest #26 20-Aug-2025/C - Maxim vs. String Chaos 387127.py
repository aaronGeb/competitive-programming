# Problem: C - Maxim vs. String Chaos - https://codeforces.com/gym/629689/problem/C

def helper(s):
    """
    This Function Help Us To calculate the prefix of chars frequency
    for both string by calling it twice
    
    """
    n = len(s)
    memo = [[0] * (n + 1) for _ in range(26)]
    for i, ch in enumerate(s, 1):
        for c in range(26):
            memo[c][i] = memo[c][i - 1]
        memo[ord(ch) - ord('a')][i] += 1
    return memo


def solve(a, b, n, q):
    freq_a = helper(a)
    freq_b = helper(b)
    
    for _ in range(q):
        left, right = map(int, input().split())
        left -= 1
        right -= 1
        ans = 0
        for c in range(26):
            count_a = freq_a[c][right + 1] - freq_a[c][left]
            count_b = freq_b[c][right + 1] - freq_b[c][left]
            if count_a > count_b:
                ans += count_a - count_b
        print(ans)

test = int(input())

for _ in range(test):
    n, q = map(int, input().split())
    a = input()
    b = input()
    solve(a, b, n, q)