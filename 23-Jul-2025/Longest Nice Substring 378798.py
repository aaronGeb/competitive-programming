# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice(sub):
            charset = set(sub)
            return all(ch.swapcase() in charset for ch in charset)
    
        n = len(s)
        max_len = 0
        result = ""
        
        for i in range(n):
            for j in range(i + 1, n):
                substr = s[i:j + 1]
                if is_nice(substr) and (j - i + 1 > max_len):
                    max_len = j - i + 1
                    result = substr
                    
        return result