# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        max_length = 1
        left = 0
        last_duplicate = -1  

        for right in range(1, len(s)):
            if s[right] == s[right - 1]:  
                if last_duplicate != -1: 
                    left = last_duplicate + 1  
                last_duplicate = right - 1  
            
            max_length = max(max_length, right - left + 1)
        
        return max_length
        