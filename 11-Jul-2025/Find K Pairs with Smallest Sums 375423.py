# Problem: Find K Pairs with Smallest Sums - https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if k == 0 or not nums1 or  not nums2:
            return []

        min_heap = []
        result = []
        for i in range(min(k,len(nums1))):
            heapq.heappush(min_heap,(nums1[i] + nums2[0],i,0)) # (sum,idx_1,idx_2)
        while min_heap and len(result)< k:
            curr_sum,i,j = heapq.heappop(min_heap)
            result.append((nums1[i],nums2[j]))
            if j +1 < len(nums2):
                heapq.heappush(min_heap,(nums1[i]+ nums2[j+1],i, j+1))
        return result
        