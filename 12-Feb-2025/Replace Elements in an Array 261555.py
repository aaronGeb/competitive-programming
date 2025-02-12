# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        map_index = {num: i for i,num in enumerate(nums)}
        for oldValue,newValue in operations:
            if oldValue in map_index:
                index = map_index[oldValue]
                nums[index] = newValue
                map_index[newValue] = index
                del map_index[oldValue]
        return nums


        