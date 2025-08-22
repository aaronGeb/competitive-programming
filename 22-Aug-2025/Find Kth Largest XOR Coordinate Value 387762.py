# Problem: Find Kth Largest XOR Coordinate Value - https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/description/?envType=problem-list-v2&envId=bit-manipulation

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        row_xor = [0] * n
        min_heap = []

        for i in range(m):
            prefix = 0
            for j in range(n):
                row_xor[j] ^= matrix[i][j]
                prefix ^= row_xor[j]
                heapq.heappush(min_heap, prefix)

                if len(min_heap) > k:
                    heapq.heappop(min_heap)

        return min_heap[0]