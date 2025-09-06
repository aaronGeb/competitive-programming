# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n =  len(piles)
        i = 0
        j =  n-1
        total_coin = 0
        while i< j:
            total_coin += piles[j-1]
            i +=1
            j -=2
        return total_coin