# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr)-1
        while right - left +1 > k:
            if abs(arr[left] - x) > abs(arr[right]-x):
                left +=1
            else:
                right -=1
        return arr[left: right+1]
