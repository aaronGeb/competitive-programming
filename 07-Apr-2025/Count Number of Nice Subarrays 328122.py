# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count_map = defaultdict(int)
        count_map[0] = 1
        
        odd_count = 0
        result = 0
        
        for num in nums:
            if num % 2 == 1:
                odd_count += 1
            result += count_map[odd_count - k]
            count_map[odd_count] += 1
            
        return result
        