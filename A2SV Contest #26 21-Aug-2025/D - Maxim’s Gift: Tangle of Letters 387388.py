# Problem: D - Maxim’s Gift: Tangle of Letters - https://codeforces.com/gym/629689/problem/D

def solve(n, text):

    if n % 2 == 0:
        even = [0 for _ in range(26)]

        odd = [0 for _ in range(26)]
        
        for i  in range(n):
            if i % 2 == 0:
                odd[ord(text[i]) - ord("a")] += 1
            else:
                even[ord(text[i]) - ord("a")] += 1
        
        # print(f"text = '{text} 'Even_max = {max(even)} Odd_max = {max(odd)}")
        return n - (max(even) + max(odd))
    else:
        suffix_even = [0 for _ in range(26)]
        suffix_odd =  [0 for _ in range(26)]
        for i  in range(n):
            if i % 2 == 0:
                suffix_odd[ord(text[i]) - ord("a")] += 1
            else:
                suffix_even[ord(text[i]) - ord("a")] += 1
        
        prefix_even = [0 for _ in range(26)]
    
        prefix_odd = [0 for _ in range(26)]
        total_max = 0
        for i in range(n):
            if i % 2 == 0:
                suffix_odd[ord(text[i]) - ord("a")] -= 1
            else:
                suffix_even[ord(text[i]) - ord("a")] -= 1
                
            max_even = 0
            
            max_odd = 0
                
            for char in range(26):
                
                max_even = max(max_even, prefix_even[char] + suffix_odd[char])
                
                max_odd = max(max_odd, prefix_odd[char] + suffix_even[char])
                
                total_max = max(total_max, max_even + max_odd)
                
            
            
            if i % 2 == 0:
                prefix_odd[ord(text[i]) - ord("a")] += 1
            else:
                prefix_even[ord(text[i]) - ord("a")] += 1
        return n - total_max
test = int(input())

for _ in range(test):
    n = int(input())
    
    text = input()
    print(solve(n, text))