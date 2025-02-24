# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

def draw_snake(n, m):
    pattern = []
    
    for i in range(1, n + 1):
        if i % 2 == 1:
            # Odd row: full snake
            pattern.append('#' * m)
        else:
            # Even row: snake in only one cell
            if (i // 2) % 2 == 1:
               
                pattern.append('.' * (m - 1) + '#')
            else:
               
                pattern.append('#' + '.' * (m - 1))
    
    return pattern

# Reading input
n, m = map(int, input().split())
result = draw_snake(n, m)

# Output the pattern
for line in result:
    print(line)