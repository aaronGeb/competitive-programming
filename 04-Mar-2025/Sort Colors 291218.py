# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        midd = 0
        right = len(nums)-1
        while midd <= right:
            if nums[midd] == 0:
                nums[left],nums[midd] = nums[midd], nums[left]
                left +=1
                midd +=1
            elif nums[midd]==1:
                midd +=1
            else:
                nums[right],nums[midd] = nums[midd], nums[right]
                right -=1

        