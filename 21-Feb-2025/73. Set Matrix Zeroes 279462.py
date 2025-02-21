# Problem: 73. Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        column = len(matrix[0])
        row_flag = col_flag = False
        for i in range(row):
            for j in range(column):
                if matrix[i][j] == 0:
                    if i == 0:
                        row_flag = True
                    if j ==0:
                        col_flag = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, row):
            for j in range(1, column):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if row_flag:
            for j in range(column):
                matrix[0][j] = 0
        if col_flag:
            for i in range(row):
                matrix[i][0] = 0