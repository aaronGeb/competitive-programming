# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        return str((((k // (k & -k)) >> 1) & 1) ^ (k & 1) ^ 1)