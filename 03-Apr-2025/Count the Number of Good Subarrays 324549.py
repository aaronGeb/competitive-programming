# Problem: Count the Number of Good Subarrays - https://leetcode.com/problems/count-the-number-of-good-subarrays/description/

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        counter = Counter()
        pairs = 0
        result = 0
        n = len(nums)
        i = 0
        for j in range(n):
            pairs += counter[nums[j]]
            counter[nums[j]] += 1
            while pairs >= k:
                result += n-j
                counter[nums[i]] -= 1
                pairs -= counter[nums[i]]
                i +=1
        return result
        