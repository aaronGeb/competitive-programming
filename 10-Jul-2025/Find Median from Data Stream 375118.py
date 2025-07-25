# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

import heapq

class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
     
    def addNum(self, num: int) -> None:
        if not self.min_heap or num >= self.min_heap[0]:
            heapq.heappush(self.min_heap, num)

        else:
            heapq.heappush(self.max_heap,-num)

        
        if len(self.min_heap) > len(self.max_heap) + 1:
            moved = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,-moved)

        elif len(self.max_heap) > len(self.min_heap):
            moved = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap,-moved)


    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]

        return (self.min_heap[0] + (-self.max_heap[0])) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()