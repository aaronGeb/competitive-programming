# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        minTime = 0
        for i, pr in enumerate(processorTime):
            minTime = max(minTime, pr + max(tasks[i*4:i*4+4]))

        return minTime

     

        