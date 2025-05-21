# Problem: Helpful Maths - https://codeforces.com/problemset/problem/339/A

def xenia_sum(s: str) -> str:
    digits = [int(ch) for ch in s if ch.isdigit()]
  
    digits.sort()
    
    return '+'.join(str(num) for num in digits)
if __name__ == "__main__":
    s = input().split(('+'))
    print(xenia_sum(s))
