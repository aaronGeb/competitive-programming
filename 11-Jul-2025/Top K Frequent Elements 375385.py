# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        min_heap = []
        for num,count in freq.items():
            heapq.heappush(min_heap,(count,num))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        return [num for count,num in min_heap]