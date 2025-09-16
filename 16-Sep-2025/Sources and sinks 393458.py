# Problem: Sources and sinks - https://basecamp.eolymp.com/en/problems/3986

import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    mat = [[int(next(it)) for _ in range(n)] for __ in range(n)]

    sources = []
    sinks = []

    for i in range(n):
        if all(mat[i][j] == 0 for j in range(n)):
            sinks.append(i + 1)  

        if all(mat[j][i] == 0 for j in range(n)):
            sources.append(i + 1)

    print(len(sources), *sources)
    print(len(sinks), *sinks)

if __name__ == "__main__":
    main()