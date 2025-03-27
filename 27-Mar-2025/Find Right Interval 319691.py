# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        import bisect
        n = len(intervals)
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))  # [(start, index)
        result = []
        
        for _, end in intervals:
            index = bisect.bisect_left(starts, (end,))  # Binary search for en
            
            if index < n:
                result.append(starts[index][1])  
            else:
                result.append(-1)
        
        return result