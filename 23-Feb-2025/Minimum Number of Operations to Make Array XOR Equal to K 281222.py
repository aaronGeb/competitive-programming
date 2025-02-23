# Problem: Minimum Number of Operations to Make Array XOR Equal to K - https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        curre_xor = 0
        for num in nums:
            curre_xor ^= num
        return bin(curre_xor^k).count('1')