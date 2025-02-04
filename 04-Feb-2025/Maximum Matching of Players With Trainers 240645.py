# Problem: Maximum Matching of Players With Trainers - https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        a, b, matches = 0,0,0
        while a < len(players) and b < len(trainers):
            if players[a] <= trainers[b]:
                matches +=1
                a +=1
            b +=1
        return matches