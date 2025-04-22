# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/description/

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for st in s:
            if st == '*':
                stack.pop()
            else:
                stack.append(st)
        return ''.join(stack)
        