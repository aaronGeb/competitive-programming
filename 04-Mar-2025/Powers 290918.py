# Problem: Powers - https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=true

 def power(n):
    for i in range(n):
        print(i**2)


if __name__ == '__main__':
    n = int(input())
    power(n)