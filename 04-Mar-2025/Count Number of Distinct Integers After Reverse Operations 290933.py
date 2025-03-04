# Problem: Count Number of Distinct Integers After Reverse Operations - https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        result = []
        for i in nums:
            result.append(i)
            if i >10:
                x = str(i)
                result.append(int(x[::-1]))
        return len(set(result))

        