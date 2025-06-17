# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(index: int, prev: int, count: int) -> bool:
            if index == len(s):
                return count >= 2  
            num = 0
            for i in range(index, len(s)):
                num = num * 10 + int(s[i])
                if prev == -1:
                    if backtrack(i + 1, num, count + 1):
                        return True
                elif prev - num == 1:
                    if backtrack(i + 1, num, count + 1):
                        return True
                elif num >= prev:
                    break  
            return False

        return backtrack(0, -1, 0)