# Problem: Count Servers that Communicate - https://leetcode.com/problems/count-servers-that-communicate/description/

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_count = [0] * m
        col_count = [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    row_count[i] += 1
                    col_count[j] += 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (row_count[i] > 1 or col_count[j] > 1):
                    ans += 1

        return ans