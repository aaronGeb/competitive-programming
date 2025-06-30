# Problem: D - Serial Time! - https://codeforces.com/gym/618729/problem/D

def read_3d_grid():
    d, r, c = map(int, input().split())
    grid = []
    layers_read = 0

    while layers_read < d:
        line = input().strip()
        if line == "":
            continue
        layer = [list(line)]
        for _ in range(r - 1):
            layer.append(list(input().strip()))
        grid.append(layer)
        layers_read += 1

    while True:
        start_line = input().strip()
        if start_line:
            break

    start_x, start_y = map(int, start_line.split())
    start_x -= 1
    start_y -= 1

    return d, r, c, grid, start_x, start_y


def in_bounds(z, x, y, d, r, c):
    return 0 <= z < d and 0 <= x < r and 0 <= y < c


def dfs(z, x, y, grid, visited, d, r, c):
    stack = [(z, x, y)]
    visited[z][x][y] = True
    minutes = 0

    directions = [
        (1, 0, 0), (-1, 0, 0),
        (0, 1, 0), (0, -1, 0),
        (0, 0, 1), (0, 0, -1)
    ]

    while stack:
        cz, cx, cy = stack.pop()
        minutes += 1

        for dz, dx, dy in directions:
            nz, nx, ny = cz + dz, cx + dx, cy + dy
            if in_bounds(nz, nx, ny, d, r, c):
                if not visited[nz][nx][ny] and grid[nz][nx][ny] == '.':
                    visited[nz][nx][ny] = True
                    stack.append((nz, nx, ny))

    return minutes


d, r, c, grid, start_x, start_y = read_3d_grid()
visited = [[[False for _ in range(c)] for _ in range(r)] for _ in range(d)]

start_layer = 0

if grid[start_layer][start_x][start_y] == '.':
    minutes_until_overflow = dfs(start_layer, start_x, start_y, grid, visited, d, r, c)
else:
    minutes_until_overflow = 0

print(minutes_until_overflow)