# Problem: Intersection of Two Arrays II - https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        my_l = []
        for i in nums1:
            if i in nums2:
                my_l.append(i)
                nums2.remove(i)
        return my_l
        