# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations) -1
        while left <= right:
            mid = (left + right) //2
            if len(citations)-mid > citations[mid]:
                left = mid +1
            else:
                right =  mid -1
        return   len(citations) - left
        