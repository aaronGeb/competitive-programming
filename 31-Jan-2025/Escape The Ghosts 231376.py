# Problem: Escape The Ghosts - https://leetcode.com/problems/escape-the-ghosts/

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        distance = abs(target[0]) + abs(target[1])
        for gost in ghosts:
            g_distance = abs(target[0] - gost[0]) + abs(target[1]- gost[1])
            if g_distance <= distance:
                return False
        return True
            