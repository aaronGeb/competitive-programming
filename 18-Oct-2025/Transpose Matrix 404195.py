# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        return [[matrix[i][k] for i in range(row)]for k in range(col)]