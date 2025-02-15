# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        # Binary search on the "flattened" matrix
        low = 0
        high = m * n - 1

        while low <= high:
            mid = (low + high) // 2
            row = mid // n  # Integer division to get the row index
            col = mid % n  # Modulo to get the column index
            mid_val = matrix[row][col]

            if mid_val == target:
                return True
            elif mid_val < target:
                low = mid + 1
            else:
                high = mid - 1

        return False
        