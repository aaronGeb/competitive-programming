# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        min_heap = []
        for i in range(min(k,n)):
            heapq.heappush(min_heap,(matrix[i][0],i,0))
        count = 0
        while min_heap:
            val,row,col = heapq.heappop(min_heap)
            count +=1
            if count ==k:
                return val
            if col +1 < n:
                heapq.heappush(min_heap,(matrix[row][col+1],row,col+1))
            
