# Problem: Game of Life - https://leetcode.com/problems/game-of-life/description/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        import numpy as np
        from scipy.signal import convolve2d
        board_np =  np.array(board)
        kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        live_neighbors = convolve2d(board, kernel, mode='same', boundary='fill', fillvalue=0)
        new_board = np.copy(board_np) 
        new_board[(board_np == 1) & ((live_neighbors < 2) | (live_neighbors > 3))] = 0 
        new_board[(board_np == 1) & ((live_neighbors == 2) | (live_neighbors == 3))] = 1
        new_board[(board_np == 0) & (live_neighbors == 3)] = 1  

        # Copy the updated values back to the original board (modifying in-place)
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = int(new_board[i][j])