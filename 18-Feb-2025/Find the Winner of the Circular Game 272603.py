# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0
        for i in range(2,n+1):
            winner = (winner +k)%i
        return winner +1 
        