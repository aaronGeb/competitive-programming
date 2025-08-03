# Problem: Interesting drink - https://codeforces.com/problemset/problem/706/B/

import bisect
 
 
def idrink(n, p, qu):
    p.sort()
    ans = []
    for m in qu:
        count = bisect.bisect_right(p, m)
        ans.append(count)
    return ans
 
 
if __name__ == "__main__":
    n = int(input())
    p = list(map(int, input().split()))
    q = int(input())
    qu = [int(input()) for _ in range(q)]
 
    ans = idrink(n, p, qu)
    print("\n".join(map(str, ans)))