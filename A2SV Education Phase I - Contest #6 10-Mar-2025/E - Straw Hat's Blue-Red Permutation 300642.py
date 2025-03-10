# Problem: E - Straw Hat's Blue-Red Permutation - https://codeforces.com/gym/594356/problem/E

def blue_red_permutation(n, a, s):
    b = []
    r = []
    for i in range(n):
        if s[i] == "B":
            b.append(a[i])
        else:
            r.append(a[i])
    b.sort()
    r.sort()
    t = sorted(range(1, n + 1))
    bptr = 0
    rptr = 0
    for i in t:
        if bptr < len(b) and b[bptr] >= i:
            bptr += 1
        elif rptr < len(r) and r[rptr] <= i:
            rptr += 1
        else:
            return "NO"
    return "YES"


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        s = input().strip()
        print(blue_red_permutation(n, a, s))


main()