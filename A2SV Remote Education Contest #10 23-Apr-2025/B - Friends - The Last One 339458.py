# Problem: B - Friends - The Last One - https://codeforces.com/gym/604857/problem/B

def solve():
    t  = int(input())
    for _ in range(t):
        n,m = map(int, input().split())
        a = list(map(int, input().split()))
        if n > m:
            print('NO')
            continue
        a_sort =  sorted(a, reverse=True)
        sum_plus = sum(a_sort) + n
        max_a = a_sort[0]
        min_a = a_sort[-1]
        if sum_plus + max_a - min_a <=m:
            print('YES')
        else:
            print('NO')
if __name__ == '__main__':
    solve()