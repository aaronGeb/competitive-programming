# Problem: Petya and Strings - https://codeforces.com/problemset/problem/112/A

def compare_strings(s1: str, s2: str) -> int:
    s1 = s1.lower()
    s2 = s2.lower()

    if s1 < s2:
        return -1
    elif s1 > s2:
        return 1
    else:
        return 0


s1 = input().strip()
s2 = input().strip()

print(compare_strings(s1, s2))
