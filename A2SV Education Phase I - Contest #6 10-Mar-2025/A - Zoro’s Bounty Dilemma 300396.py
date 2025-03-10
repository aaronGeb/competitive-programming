# Problem: A - Zoro’s Bounty Dilemma - https://codeforces.com/gym/594356/problem/A

def zoro():
    t = int(input())  
    for _ in range(t):
        dt = input().strip() 
        
        if '<' in dt and '>' in dt:
            print('?') 
        elif '<' in dt:
            print('<')  
        elif '>' in dt:
            print('>')  
        else:
            print('=')  
if __name__ == "__main__":
  zoro()