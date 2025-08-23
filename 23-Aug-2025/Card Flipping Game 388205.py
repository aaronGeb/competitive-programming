# Problem: Card Flipping Game - https://leetcode.com/problems/card-flipping-game/description/

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        data = set(fronts + backs)
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                data.discard(fronts[i])
        if data:
            return(min(data))
        else:
            return 0