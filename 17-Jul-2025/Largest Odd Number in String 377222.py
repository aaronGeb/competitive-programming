# Problem: Largest Odd Number in String - https://leetcode.com/problems/largest-odd-number-in-string/

class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        for i in range(n - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i + 1]
        return ""