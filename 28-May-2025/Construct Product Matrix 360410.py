# Problem: Construct Product Matrix - https://leetcode.com/problems/construct-product-matrix/description/

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        total = n * m
        MOD = 12345

        # Flatten the matrix
        flat = []
        for row in grid:
            flat.extend(row)

        # Prefix and suffix product arrays
        prefix = [1] * total
        suffix = [1] * total

        for i in range(1, total):
            prefix[i] = (prefix[i - 1] * flat[i - 1]) % MOD

        for i in range(total - 2, -1, -1):
            suffix[i] = (suffix[i + 1] * flat[i + 1]) % MOD

        # Build result from prefix * suffix
        result = []
        for i in range(n):
            row = []
            for j in range(m):
                idx = i * m + j
                val = (prefix[idx] * suffix[idx]) % MOD
                row.append(val)
            result.append(row)

        return result