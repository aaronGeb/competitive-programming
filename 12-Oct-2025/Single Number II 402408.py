# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(32): 
            bit_sum = 0
            for num in nums:
                bit_sum += (num >> i) & 1
            bit_sum %= 3
            if bit_sum:
                result |= (1 << i)

        if result >= 2**31:
            result -= 2**32
        return result