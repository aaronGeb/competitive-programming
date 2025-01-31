# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occured = {}
        for i, char in enumerate(s):
            last_occured[char] = i
        seen = set()
        stack = []
        for i,char in enumerate(s):
            if char in seen:
                continue 
            while stack and char < stack[-1] and last_occured[stack[-1]] >i:
                remove_char = stack.pop()
                seen.remove(remove_char)
            stack.append(char)
            seen.add(char)
        return ''.join(stack)

  
        