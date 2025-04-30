# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1/(self.myPow(x,-n))
        if n == 0:
            return 1
        mid = self.myPow(x,n//2)
        if n%2==0:
            return mid * mid
        else:
            return mid * mid *x