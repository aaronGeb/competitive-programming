# Problem: Maximal Network Rank - https://leetcode.com/problems/maximal-network-rank/description/

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        connected = [[False]*n for _ in range(n)]

        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
            connected[a][b] = True
            connected[b][a] = True

        max_rank = 0
        for i in range(n):
            for j in range(i + 1, n):
                rank = degree[i] + degree[j]
                if connected[i][j]:
                    rank -= 1
                max_rank = max(max_rank, rank)

        return max_rank