# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(num for num in nums if num%2==0)
        result = []
        for value,index in queries:
            if nums[index] %2==0:
                even_sum -= nums[index]
            nums[index] += value
            if nums[index]%2==0:
                even_sum += nums[index]
            result.append(even_sum)
        return result
        