# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(combinations(range(1, n + 1), k))