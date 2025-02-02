# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        for i in range(n):
            if nums[i]!=0:
                target_index = (i+ nums[i]%n + n)%n
                result.append(nums[target_index])
            else:
                result.append(0)
        return result

        