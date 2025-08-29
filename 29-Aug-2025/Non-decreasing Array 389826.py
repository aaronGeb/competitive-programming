# Problem: Non-decreasing Array - https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modificaton = 0
        n = len(nums)
        for i in range(1,n):
            if nums[i] < nums[i-1]:
                modificaton +=1
                if modificaton > 1:
                    return False
                if i>=2 and nums[i] < nums[i-2]:
                    nums[i] = nums[i-1]
                else:
                    nums[i-1] = nums[i]
        return True


        