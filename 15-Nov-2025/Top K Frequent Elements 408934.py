# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = [(-count,num) for num,count in freq.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for  _ in range(k)]