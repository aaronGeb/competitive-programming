# Problem: E - The Case of the Missing Operations - https://codeforces.com/gym/622136/problem/E

import sys
import heapq

input = sys.stdin.read
feat = input().splitlines()


n = int(feat[0])
heap = []
res = []
ops = feat[1:]
for line in ops:
    part = line.split()
    if part[0] == "insert":
        x = int(part[1])
        heapq.heappush(heap, x)
        res.append(f"insert {x}")
    elif part[0] == "getMin":
        x = int(part[1])
        while heap and heap[0] < x:
            heapq.heappop(heap)
            res.append(f"removeMin")

        if not heap or heap[0] > x:
            heapq.heappush(heap, x)
            res.append(f"insert {x}")
        res.append(f"getMin {x}")
    elif part[0] == "removeMin":
        if not heap:
            res.append('insert 0')
            heapq.heappush(heap, 0)
        heapq.heappop(heap)
        res.append("removeMin")
print(len(res))
print("\n".join(res))
