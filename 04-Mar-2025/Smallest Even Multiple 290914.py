# Problem: Smallest Even Multiple - https://leetcode.com/problems/smallest-even-multiple/

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
      return n if n%2==0 else 2*n
        