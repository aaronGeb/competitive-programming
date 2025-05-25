# Problem: Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

def smallest_array(n, a):
    has_even = any(x % 2 == 0 for x in a)
    has_odd = any(x % 2 == 1 for x in a)

    if has_even and has_odd:
        return sorted(a)
    else:
        return a

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    result = smallest_array(n, a)
    print(*result)
