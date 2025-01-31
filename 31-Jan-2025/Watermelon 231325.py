# Problem: Watermelon - https://codeforces.com/problemset/problem/4/A

def can_divide_watermelon(w):
    if w > 2 and w % 2 == 0:
        return "YES"
    else:
        return "NO"


# Read input
if __name__ == "__main__":
    w = int(input())
    print(can_divide_watermelon(w))