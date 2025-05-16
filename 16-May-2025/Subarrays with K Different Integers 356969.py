# Problem: Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(k):
            count = defaultdict(int)
            res = i = 0
            for j in range(len(nums)):
                if count[nums[j]] == 0:
                    k -= 1
                count[nums[j]] += 1
                while k < 0:
                    count[nums[i]] -= 1
                    if count[nums[i]] == 0:
                        k += 1
                    i += 1
                res += j - i + 1
            return res
        
        return atMostK(k) - atMostK(k - 1)