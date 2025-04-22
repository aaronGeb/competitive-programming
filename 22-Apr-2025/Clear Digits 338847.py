# Problem: Clear Digits - https://leetcode.com/problems/clear-digits/description/

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for d in s:
            if d.isdigit():
                stack.pop()
            else:
                stack.append(d)
        return ''.join(stack)