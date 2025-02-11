# Problem: Maximum-sum-of-distinct-subarrays-with-length-k - https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        current_sum = 0
        result = 0
        left = 0
        for right in range(len(nums)):
            current_sum +=nums[right]
            count[nums[right]] +=1
            if right -left +1 >k:
                count[nums[left]] -=1
                if count[nums[left]] ==0:
                    count.pop(nums[left])
                current_sum -= nums[left]
                left +=1

            if len(count) == k and right- left +1==k:
                result = max(result,current_sum)
        return result