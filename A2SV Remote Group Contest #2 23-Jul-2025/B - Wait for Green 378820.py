# Problem: B - Wait for Green - https://codeforces.com/gym/623571/problem/B

import sys
 
def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, c = sys.stdin.readline().split()
        n = int(n)
        s = sys.stdin.readline().strip()
        if c == 'g':
            print(0)
            continue
        green_positions = []
        for i, char in enumerate(s):
            if char == 'g':
                green_positions.append(i)
        max_wait = 0
        for i, char in enumerate(s):
            if char == c:
                left = 0
                right = len(green_positions) - 1
                found = -1
                while left <= right:
                    mid = (left + right) // 2
                    if green_positions[mid] >= i:
                        found = mid
                        right = mid - 1
                    else:
                        left = mid + 1
                if found != -1:
                    wait = green_positions[found] - i
                else:
                    wait = (n - i) + green_positions[0]
                max_wait = max(max_wait, wait)
        print(max_wait)
 
solve()