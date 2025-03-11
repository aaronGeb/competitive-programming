# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        chemistry = 0
        team_sum = skill[0] + skill[n-1]
        left = 0
        right = n-1
        while left < right:
            if skill[left] + skill[right] != team_sum:
                return -1
            chemistry += skill[left]* skill[right]
            left +=1
            right -=1
        return chemistry
