# Problem: Binary Number with Alternating Bits - https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary = bin(n)[2:]
        n = len(binary)
        for i in range(n-1):
            if binary[i] == binary[i+1]:
                return False
        return True
        