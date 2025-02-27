# Problem: Maximum Matrix Sum - https://leetcode.com/problems/maximum-matrix-sum/description/?envType=problem-list-v2&envId=matrix

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        max_sum = 0
        current_value = float('inf')
        count = 0
        for row in matrix:
            for num in row:
                max_sum += abs(num)
                current_value = min(current_value,abs(num))
                if num < 0:
                    count +=1
        if count %2 == 1:
            max_sum  -=2*current_value
        return max_sum     