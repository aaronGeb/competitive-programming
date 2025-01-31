# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

def love_story(test_case):
    target = "codeforces"
    n = len(target)
    for s in test_case:
        count = sum(1 for i in range(10) if s[i] != target[i])
        print(count)


if __name__ == "__main__":
    t = int(input())
    test_case = [input().strip() for _ in range(t)]
    love_story(test_case)