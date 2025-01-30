# Problem: Arithmetic Operators - https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true

def mathOperation(a,b):
    print(f'{a+b}\n{a-b}\n{a*b}')
    

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    mathOperation(a,b)