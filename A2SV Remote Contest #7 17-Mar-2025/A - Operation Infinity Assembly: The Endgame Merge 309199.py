# Problem: A - Operation Infinity Assembly: The Endgame Merge - https://codeforces.com/gym/596004/problem/A

def smallest_string(t, test_cases):
    results = []
    
    for case in test_cases:
        n, m, k, a, b = case
 
        a = sorted(a)
        b = sorted(b)
        
        i, j = 0, 0 
        c = []      
        count_a = 0  
        count_b = 0  
        
        while i < n and j < m:
            if (a[i] < b[j] and count_a < k) or count_b == k:
                c.append(a[i])
                i += 1
                count_a += 1
                count_b = 0 
            else:
                c.append(b[j])
                j += 1
                count_b += 1
                count_a = 0  
        
        results.append("".join(c))
    
    return results
 
t = int(input())  
test_cases = []
 
for _ in range(t):
    n, m, k = map(int, input().split())
    a = input().strip()
    b = input().strip()
    test_cases.append((n, m, k, a, b))
 
# Solve and print results
for result in smallest_string(t, test_cases):
    print(result)