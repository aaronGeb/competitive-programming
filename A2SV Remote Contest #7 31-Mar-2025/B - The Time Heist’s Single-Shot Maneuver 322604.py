# Problem: B - The Time Heist’s Single-Shot Maneuver - https://codeforces.com/gym/596004/problem/B

import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n, m = map(int, input[ptr:ptr+2])
        ptr +=2
        a = list(map(int, input[ptr:ptr+n]))
        ptr +=n
        b = list(map(int, input[ptr:ptr+m]))
        ptr +=m
        
        b_val = b[0]
        possible = True
      
        prev_choices = [a[0], b_val - a[0]]
        
        for i in range(1, n):
            current_original = a[i]
            current_transformed = b_val - a[i]
            new_choices = []
            
            for prev in prev_choices:
                if current_original >= prev:
                    new_choices.append(current_original)
                    break
            
            for prev in prev_choices:
                if current_transformed >= prev:
                    new_choices.append(current_transformed)
                    break
           
            prev_choices = list(set(new_choices))  
            if not prev_choices:
                possible = False
                break
        print("YES" if possible else "NO")

solve()