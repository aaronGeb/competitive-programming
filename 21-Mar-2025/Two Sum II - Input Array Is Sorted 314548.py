# Problem: Two Sum II - Input Array Is Sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while l< r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l +1, r+1]
            elif total > target:
                r -=1
            else:
                l +=1
        