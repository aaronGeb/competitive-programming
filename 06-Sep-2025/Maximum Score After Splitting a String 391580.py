# Problem: Maximum Score After Splitting a String - https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        left = 0
        right = s.count("1")
        result = 0
        for num in s[:-1]:
            left += int(num) ^ 1
            right  -= int(num)
            result = max(result, left+ right)
        return result