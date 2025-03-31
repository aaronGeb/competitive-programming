# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currentSum = 0
        count = 0
        mymap = {0:1}
        for num in nums:
            currentSum += num
            if currentSum -k in mymap:
                count += mymap[currentSum - k]
            if currentSum in mymap:
                mymap[currentSum] +=1
            else:
                mymap[currentSum] = 1
        return count
        