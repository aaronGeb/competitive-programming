# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        '''
        f(n) = (x**n - y**n)/sqrt(5)
        '''
        sqrt_5 = math.sqrt(5)
        phi = (1+ sqrt_5)/2
        psi = (1- sqrt_5)/2
        finb_n = (phi**n - psi**n)/sqrt_5
        return round(finb_n)