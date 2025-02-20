# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        import numpy as np
        numpy_array = np.array(matrix)
        numpy_transpose = numpy_array .T
        numpy_to_list  = numpy_transpose.tolist()
        return numpy_to_list
        