class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            x = 1/x
            n = -n
        temp = 1.0
        while n > 0:
            if n % 2 == 1:
                temp *= x
            x *= x
            n //= 2
        return temp
