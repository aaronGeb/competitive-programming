# Problem: Palindromic Substrings - https://leetcode.com/problems/palindromic-substrings/description/

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for center in range(len(s)):
            for right in [center, center+1]:
                left = center
                while left >=0 and right < len(s) and s[left] == s[right]:
                    count +=1
                    left -=1
                    right +=1
        return count