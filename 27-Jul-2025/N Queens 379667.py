# Problem: N Queens - https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []

        def backtrack(row, cols, diags, anti_diags, board):
            if row == n:
                results.append(["".join(r) for r in board])
                return
            
            for col in range(n):
                if col in cols or (row - col) in diags or (row + col) in anti_diags:
                    continue

                board[row][col] = 'Q'
                cols.add(col)
                diags.add(row - col)
                anti_diags.add(row + col)

                backtrack(row + 1, cols, diags, anti_diags, board)

                board[row][col] = '.'
                cols.remove(col)
                diags.remove(row - col)
                anti_diags.remove(row + col)

        empty_board = [['.'] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), empty_board)
        return results