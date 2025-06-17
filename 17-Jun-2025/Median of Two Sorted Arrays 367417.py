# Problem: Median of Two Sorted Arrays - https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median=0
        nums1[:]=nums1+nums2
        nums1.sort()
        n=len(nums1)
        
        if n%2==0:
            l=(n//2)-1
            r=(n//2)
            median=(nums1[l]+nums1[r])/2
        else:
            r=(n//2)
            median=(nums1[r])
        return median