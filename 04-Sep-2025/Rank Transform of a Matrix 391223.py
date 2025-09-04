# Problem: Rank Transform of a Matrix - https://leetcode.com/problems/rank-transform-of-a-matrix/

class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        rank = [0] * (m + n)

        # Sort the elements
        value_cells = defaultdict(list)
        for i in range(m):
            for j in range(n):
                value_cells[matrix[i][j]].append((i, j))

        ans = [[0] * n for _ in range(m)]

        for value in sorted(value_cells):
            parent = {}

            def find(x):
                parent.setdefault(x, x)
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]

            # Union rows and columns
            for i, j in value_cells[value]:
                parent_i = find(i)
                parent_j = find(j + m)
                parent[parent_i] = parent_j

            group_max_rank = defaultdict(int)
            for i, j in value_cells[value]:
                root = find(i)
                group_max_rank[root] = max(group_max_rank[root], rank[i], rank[j + m])

            for i, j in value_cells[value]:
                root = find(i)
                ans[i][j] = group_max_rank[root] + 1
                rank[i] = rank[j + m] = ans[i][j]

        return ans