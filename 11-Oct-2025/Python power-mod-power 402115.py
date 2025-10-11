# Problem: Python power-mod-power - https://www.hackerrank.com/challenges/python-power-mod-power/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
a  = int(input())
b = int(input())
c =  int(input())
power = a**b
result = (a**b)%c
print(power)
print(result)