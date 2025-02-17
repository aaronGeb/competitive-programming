def construct_matrix(n):
    if n == 2:
        return "-1"
 
   
    odds = list(range(1, n*n + 1, 2))
    evens = list(range(2, n*n + 1, 2))
 
   
    numbers = odds + evens
 
    
    matrix = [[0] * n for _ in range(n)]
    idx = 0
 
    for i in range(n):
        for j in range(n):
            matrix[i][j] = numbers[idx]
            idx += 1
 
   
    return "\n".join(" ".join(map(str, row)) for row in matrix)
 
# Read input
t = int(input().strip())
results = []
for _ in range(t):
    n = int(input().strip())
    results.append(construct_matrix(n))
 
 
print("\n".join(results))