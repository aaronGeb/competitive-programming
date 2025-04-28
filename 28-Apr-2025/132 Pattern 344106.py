# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        i = -inf
        stack = []
        for j in nums[::-1]:
            if j < i:
                return True
            while stack and stack[-1] < j:
                i = stack.pop()
            stack.append(j)
        return False
        