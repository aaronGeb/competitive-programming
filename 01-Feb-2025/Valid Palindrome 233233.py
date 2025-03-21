# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = ''.join(char.lower() for char in s if char.isalnum())
        return filtered_s == filtered_s[::-1]
       
        