# Problem: B - Thousand Sunny's Network Setup - https://codeforces.com/gym/594356/problem/B

def network_setup(r,t):
    a = list(map(int, input().split()))  
    a.sort()
    print(a[r - t])


if __name__ == "__main__":
  r, t = map(int, input().split()) 
  network_setup(r,t)