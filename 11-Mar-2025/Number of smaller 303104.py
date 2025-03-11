# Problem: Number of smaller - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

import bisect
def number_of_smaller():
   n,m = map (int, input().split())
   arr1 = list(map(int, input().split()))
   arr2 = list(map(int, input().split()))
   result = [bisect.bisect_left(arr1, x) for x in arr2]
   print(*result)
 

if __name__ == "__main__":
    number_of_smaller()