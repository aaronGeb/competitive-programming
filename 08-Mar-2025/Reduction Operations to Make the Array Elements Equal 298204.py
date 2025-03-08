# Problem: Reduction Operations to Make the Array Elements Equal - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        ans = 0 
        nums.sort(reverse = True)
        uni = nums[0]
        for i in range(1,len(nums)):
            if uni > nums[i]:
                ans+=i
                uni = nums[i]
        return ans
        