# Problem: Construct Quad Tree - https://leetcode.com/problems/construct-quad-tree/description/

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(r1, c1, r2, c2):
            has_zero = has_one = False
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    if grid[i][j] == 0:
                        has_zero = True
                    else:
                        has_one = True
                    if has_zero and has_one:
                        break
                if has_zero and has_one:
                    break

            if not (has_zero and has_one):
                return Node(grid[r1][c1], True)

            mid_r, mid_c = (r1 + r2) // 2, (c1 + c2) // 2
            return Node(
                val=1,  
                isLeaf=False,
                topLeft=dfs(r1, c1, mid_r, mid_c),
                topRight=dfs(r1, mid_c + 1, mid_r, c2),
                bottomLeft=dfs(mid_r + 1, c1, r2, mid_c),
                bottomRight=dfs(mid_r + 1, mid_c + 1, r2, c2),
            )

        n = len(grid)
        return dfs(0, 0, n - 1, n - 1)
