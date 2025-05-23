# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        if not s or len(s) == 1:
            return s
    
        longest = ""
    
        for i in range(len(s)):
        # Odd length palindromes
            odd_palindrome = expandAroundCenter(i, i)
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
        
        # Even length palindromes
            even_palindrome = expandAroundCenter(i, i + 1)
            if len(even_palindrome) > len(longest):
                longest = even_palindrome
    
        return longest