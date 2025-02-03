# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win_count = defaultdict(int)
        loss_count = defaultdict(int)
        for winner,loss in matches:
            win_count[winner] +=1
            loss_count[loss] +=1
        zero_loss = sorted([player for player in win_count if loss_count[player] == 0])
        one_loss = sorted([player for player in loss_count if loss_count[player]==1])
        return [zero_loss, one_loss]
        