# Problem: C - Loopix: The Book Cycle - https://codeforces.com/gym/632067/problem/C

def solve():
   
    n = int(input())
    p = [int(x) - 1 for x in input().split()]
    answers = [0] * n
    
    for i in range(n):
       
        if answers[i] == 0:
          
            path = []
            current_kid = i
            while True:
                path.append(current_kid)
                current_kid = p[current_kid]
                if current_kid == i:
                    break
            
            cycle_length = len(path)
            for kid_in_path in path:
                answers[kid_in_path] = cycle_length
    print(*answers)
q = int(input())
for _ in range(q):
    solve()