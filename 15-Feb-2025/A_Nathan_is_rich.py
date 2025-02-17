def min_vehicles(t, cases):
    results = []
    for n in cases:
        results.append(n // 4 + (1 if n % 4 else 0))
    return results
 
# Read input
t = int(input())  
cases = [int(input()) for _ in range(t)]
 

for res in min_vehicles(t, cases):
    print(res)