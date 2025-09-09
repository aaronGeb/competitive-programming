# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        counts = Counter( i %k for i in arr)
        return counts[0]%2==0 and all(counts[i]== counts[k-i] for i in range(1,k))
      