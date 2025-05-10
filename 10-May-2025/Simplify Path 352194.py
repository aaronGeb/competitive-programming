# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for s in path.split('/'):
            if not s or s == '.':
                continue
            if s == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(s)
        return '/' + '/'.join(stack)
        