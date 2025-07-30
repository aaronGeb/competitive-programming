# Problem: Topological Sort - https://codeforces.com/problemset/gymProblem/101102/K

import sys
import threading
from collections import defaultdict
import heapq

def main():
    import sys
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        
       
        removed_edges = set()
        for _ in range(M):
            a, b = map(int, input().split())
            removed_edges.add((a, b))

        graph = defaultdict(list)
        in_degree = [0] * (N + 1)

        for u in range(1, N + 1):
            for v in range(u + 1, N + 1):
                if (u, v) not in removed_edges:
                    graph[u].append(v)
                    in_degree[v] += 1

        heap = []
        for i in range(1, N + 1):
            if in_degree[i] == 0:
                heapq.heappush(heap, -i)  

        result = []
        while heap:
            node = -heapq.heappop(heap)
            result.append(node)
            for nei in graph[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    heapq.heappush(heap, -nei)

        print(' '.join(map(str, result)))
main()