# Problem: Weird - https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys
def weird_num(n):
    if n%2==1:
        print('Weird')
    elif n%2==0 and 2<=n<=5:
        print('Not Weird')
    elif n%2==0 and 6<=n<=20:
        print('Weird')
    elif n%2==0 and n>20:
        print('Not Weird')


if __name__ == '__main__':
    n = int(input().strip())
    weird_num(n)
    
