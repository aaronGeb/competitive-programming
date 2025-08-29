# Problem: C - Xorion: The Subsegment Showdown - https://codeforces.com/gym/630556/problem/C

test = int(input())
for _ in range(test):
    x, y = map(int, input().split())
    
    diff = x ^ y
    ans = 1
    
    
    while diff & 1 == 0 and diff != 0:
        ans <<= 1
        diff >>= 1
    
    print(ans)