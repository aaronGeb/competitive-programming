# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <=1:
            return nums
        n = len(nums)
        mid = n//2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left,right)


    def merge(self,left,right):
        arr = []
        i =j = 0
        while i <len(left) and j < len(right):
            if left[i] < right[j]:
                arr.append(left[i])
                i +=1
            else:
                arr.append(right[j])
                j +=1
        arr.extend(left[i:])
        arr.extend(right[j:])
        return arr