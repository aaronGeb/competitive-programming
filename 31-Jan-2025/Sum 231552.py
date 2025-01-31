# Problem: Sum - https://codeforces.com/contest/1742/problem/A

def sum_total(test_case):
    for a, b, c in test_case:
        if a + b == c or a + c == b or b + c == a:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    t = int(input())
    test_case = [list(map(int, input().split())) for i in range(t)]
    sum_total(test_case)