# Problem: Subsets II - https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        def backtruck(start,path):
            res.append(path[:])
            for i in range(start,n):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtruck(i+1,path)
                path.pop()
        backtruck(0,[])
        return res
