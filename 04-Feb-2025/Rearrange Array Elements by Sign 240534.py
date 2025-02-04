# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        for num in nums:
            if num >0:
                positive.append(num)
            else:
                negative.append(num)
        result = []
        n = len(positive)
        for i in range(n):
            result.append(positive[i])
            result.append(negative[i])
        return result

        