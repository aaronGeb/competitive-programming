# Problem: Put Marbles in Bags - https://leetcode.com/problems/put-marbles-in-bags/

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1 :
            return 0
        
        n = len(weights)
        if n == 2:
            return 0
        arr = [weights[i] + weights[i + 1] for i in range(n - 1)]
        arr.sort()
        min_sum = sum(arr[:k - 1])
        max_sum = sum(arr[-(k - 1):])
        return max_sum - min_sum