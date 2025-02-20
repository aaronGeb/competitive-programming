# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        import numpy as np
        if not mat:
            return []
        numpy_array = np.array(mat)
        row,column =  numpy_array.shape
        result  = []
        # there are (row + column - 1) diagonals
        for dig in range(row + column-1):
            if dig < column:
                r,c = 0,dig
            else:
                r,c = dig - column + 1, column - 1
            diagonal = []
            while r < row and c >= 0:
                diagonal.append(numpy_array[r,c])
                r +=1
                c -= 1
            if dig %2 == 0:
                diagonal.reverse()
            result.extend(diagonal)
        return [int(x) for x in result]