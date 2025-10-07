# Problem: Find the Index of the First Occurrence in a String - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        for k in range(n - m + 1):
            if haystack[k : k + m] == needle:
                return k
        return -1