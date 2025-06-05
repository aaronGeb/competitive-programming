# Problem: The k-th Lexicographical String of All Happy Strings of Length n - https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = []

        def backtrack(curr):
            if len(result) == k:
                return
            if len(curr) == n:
                result.append(curr)
                return
            
            for ch in ['a', 'b', 'c']:
                if not curr or curr[-1] != ch:
                    backtrack(curr + ch)
        
        backtrack("")

        return result[k - 1] if k <= len(result) else ""