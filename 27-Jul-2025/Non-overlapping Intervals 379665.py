# Problem: Non-overlapping Intervals - https://leetcode.com/problems/non-overlapping-intervals/description/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
    
        count = 0
        end = float('-inf')
        
        for start, finish in intervals:
            if start >= end:
                end = finish 
            else:
                count += 1

        return count