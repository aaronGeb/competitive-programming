# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while (mask &b)>0:
            a , b= a^b,(a & b)<<1
        return (a & mask) if b > 0 else a