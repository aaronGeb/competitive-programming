# Problem: E - The beautiful String - https://codeforces.com/gym/586622/problem/E

from sys import stdin, stdout

def ini():
    return int(stdin.readline().strip())
def inli():
    return list(map(int, stdin.readline().strip().split()))
def inls():
    return stdin.readline().strip().split()
def ins():
    return stdin.readline().strip()
def inlc():
    return list(stdin.readline().strip())
def inli2():
    return list(map(int, stdin.readline().strip()))

def solve():
    check = [1, 1, 0, 0]
    s = inli2()
    q = ini()
    if len(s) < 4:
        for _ in range(q):
            stdin.readline()
            print("NO")
        return

    count = 0
    for i in range(0, len(s) - 3):
        if s[i:i+4] == check:
            count += 1

    for _ in range(q):
        query = inli()
        i = query[0] - 1
        v = query[1]

        old_count = 0

        small = max(0, i-3)
        big = min(len(s)-3, i+1)
        for j in range(small, big):
            if s[j:j+4] == check:
                old_count += 1

        s[i] = v

        new_count = 0
        for j in range(small, big):
            if s[j:j+4] == check:
                new_count += 1
        
        change = new_count - old_count
        count += change
            
        if count > 0:
            print("YES")
        else:
            print("NO")

def main():
    tc = ini()
    for _ in range(tc):
        solve()

if __name__ == "__main__":
    main()