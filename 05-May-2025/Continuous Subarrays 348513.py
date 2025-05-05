# Problem: Continuous Subarrays - https://leetcode.com/problems/continuous-subarrays/

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        result = 0
        i = 0
        s = SortedList()
        for num in nums:
            s.add(num)
            while s[-1] - s[0]  > 2:
                s.remove(nums[i])
                i +=1
            result += len(s)
        return result