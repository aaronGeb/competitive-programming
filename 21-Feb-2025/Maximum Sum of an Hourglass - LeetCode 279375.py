# Problem: Maximum Sum of an Hourglass - LeetCode - https://leetcode.com/problems/maximum-sum-of-an-hourglass/description/

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        column = len(grid[0])
        max_sum = float('-inf')
        for i in range(rows-2):
            for k in range(column -2):
                top = sum(grid[i][k:k+3])
                middle = grid[i+1][k+1]
                bottom = sum(grid[i+2][k:k+3])
                _sum = top + middle + bottom
                max_sum = max(max_sum, _sum)
        return  max_sum    