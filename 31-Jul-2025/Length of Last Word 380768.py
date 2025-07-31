# Problem: Length of Last Word - https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        idx = len(s)-1
        length = 0
        while idx >=0 and s[idx]==" ":
            idx -=1
        while idx >=0 and s[idx] !=" ":
            length +=1
            idx -=1
        return length

