# Problem: Knight Probability in Chessboard - https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[0.0] * n for _ in range(n)]
        dp[row][column] = 1.0

        # All 8 possible moves for a knight
        moves = [
                (1, 2), (1, -2), (-1, 2), (-1, -2),
                (2, 1), (2, -1), (-2, 1), (-2, -1)
                ]
        for _ in range(k):
            next_dp = [[0.0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    if dp[r][c] > 0:
                        for dr, dc in moves:
                            next_r, next_c = r + dr, c + dc
                            if 0 <= next_r < n and 0 <= next_c < n:
                                next_dp[next_r][next_c] += dp[r][c] / 8.0
            dp = next_dp
        return sum(sum(r) for r in dp)
