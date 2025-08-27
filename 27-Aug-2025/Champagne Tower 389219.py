# Problem: Champagne Tower - https://leetcode.com/problems/champagne-tower/

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0.0] * (query_row + 2) for _ in range(query_row + 2)]
        dp[0][0] = poured

        for r in range(query_row + 1):
            for c in range(r + 1):
                if dp[r][c] > 1:
                    overflow = (dp[r][c] - 1) / 2.0
                    dp[r+1][c] += overflow
                    dp[r+1][c+1] += overflow
                    dp[r][c] = 1  

        return min(1, dp[query_row][query_glass])