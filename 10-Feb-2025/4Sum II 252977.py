# Problem: 4Sum II - https://leetcode.com/problems/4sum-ii/

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_ab = defaultdict(int)
        
        for a in nums1:
            for b in nums2:
                sum_ab[a + b] += 1
        count = 0
        for c in nums3:
            for d in nums4:
                count += sum_ab[-(c + d)]  
        
        return count
        