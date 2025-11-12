# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occ = {val: i for i, val in enumerate(s)}
        stack = []
        seen = set()

        for i, c in enumerate(s):
            if c in seen:
                continue
            while stack and c < stack[-1] and last_occ[stack[-1]] > i:
                seen.remove(stack.pop())
            stack.append(c)
            seen.add(c)

        return ''.join(stack)