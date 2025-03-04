# Problem: Mod Power - https://www.hackerrank.com/challenges/python-power-mod-power/problem?isFullScreen=true

def mod_operation(a,b,m):
    pow = a**b
    print(pow)
    print(pow%m)
    
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    m = int(input())
    mod_operation(a,b,m)