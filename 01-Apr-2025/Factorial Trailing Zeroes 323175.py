# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n >=5:
            count += n//5
            n //=5
        return count 
        