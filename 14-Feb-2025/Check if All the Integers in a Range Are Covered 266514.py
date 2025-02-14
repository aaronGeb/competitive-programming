# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        covered = set()
    
        for start, end in ranges:
            covered.update(range(start, end + 1))

        return all(num in covered for num in range(left, right + 1))