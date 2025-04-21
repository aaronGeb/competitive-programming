# Problem: Greetings - https://codeforces.com/contest/1915/problem/F

from bisect import bisect_left
import sys
input = sys.stdin.read

def count_inversions(arr):
    sorted_arr = sorted(set(arr))
    ranks = {v: i+1 for i, v in enumerate(sorted_arr)} 
    bit = [0] * (len(sorted_arr) + 2)
    
    def update(idx):
        while idx < len(bit):
            bit[idx] += 1
            idx += idx & -idx

    def query(idx):
        res = 0
        while idx > 0:
            res += bit[idx]
            idx -= idx & -idx
        return res

    inversions = 0
    for x in reversed(arr):
        rank = ranks[x]
        inversions += query(rank - 1)
        update(rank)
    return inversions

def solve(data):
    output = []
    idx = 0
    t = int(data[idx])
    idx += 1
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        people = []
        for _ in range(n):
            a, b = map(int, data[idx].split())
            people.append((a, b))
            idx += 1
        people.sort()
        b_list = [b for a, b in people]
        result = count_inversions(b_list)
        output.append(str(result))
    return "\n".join(output)
data = input().splitlines()
print(solve(data))