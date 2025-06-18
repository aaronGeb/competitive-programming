# Problem: Smallest Value After Replacing With Sum of Prime Factors - https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def smallestValue(self, n: int) -> int:
        def sum_of_prime_factors(x):
            total = 0
            i = 2
            while i * i <= x:
                while x % i == 0:
                    total += i
                    x //= i
                i += 1
            if x > 1:
                total += x
            return total
        
        while True:
            next_n = sum_of_prime_factors(n)
            if next_n == n:
                return n
            n = next_n