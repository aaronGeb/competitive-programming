# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        res = 0
        n = 0
        for i, val in enumerate(s):
            if val == '(':
                n += 1
            else:
                n -= 1
                if s[i-1] == '(':
                    res += 1<< n
        return res
        