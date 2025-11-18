# Problem: Perfect Squares - https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        def is_square(x: int) -> bool:
            r = int(math.isqrt(x))
            return r * r == x
        if is_square(n):
            return 1
        for i in range(1, int(math.isqrt(n)) + 1):
            if is_square(n - i*i):
                return 2
        m = n
        while m % 4 == 0:
            m //= 4
        if m % 8 == 7:
            return 4
        return 3