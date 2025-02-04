# Problem: Maximum Product of Three Numbers - https://leetcode.com/problems/maximum-product-of-three-numbers/description/

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        max_product_2 = nums[-1]* nums[-2] * nums[-3]
        max_product_1 = nums[1]* nums[0] * nums[-1]
        return max(max_product_2,max_product_1)
        