# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count = defaultdict(int)
        result = 0
        # Count occurrences of each product
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                count[nums[i] * nums[j]] += 1

        # Calculate valid tuples
        for c in count.values():
            if c > 1:
                result += (c * (c - 1) // 2) * 8 

        return result
        