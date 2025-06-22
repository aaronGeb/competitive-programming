# Problem: Operations on Graph - https://www.eolymp.com/en/contests/9060/problems/78602

from collections import defaultdict

n = int(input())
k = int(input())

adjList = defaultdict(list)

for _ in range(k):
    
    ins = list(map(int, input().split()))
    
    if ins[0] == 1:
        adjList[ins[1]].append(ins[2])
        adjList[ins[2]].append(ins[1])
        
    elif len(adjList[ins[1]]) > 0:
        print(*adjList[ins[1]])