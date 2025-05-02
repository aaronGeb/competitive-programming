# Problem: Print 1 to n without using loops - https://www.geeksforgeeks.org/print-1-to-n-without-using-loops/

def printNos(n):
    if n > 0:
        printNos(n - 1)
        print(n, end=' ')

n = 10
printNos(n)