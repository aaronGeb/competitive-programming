# Problem: Find the Number of Distinct Colors Among the Balls - https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colorMap = {}
        ballMap = {}
        res = []
        for ball,color in queries:
            if ball in ballMap:
                prev_color = ballMap[ball]
                colorMap[prev_color]-=1
                if colorMap[prev_color] ==0:
                    del colorMap[prev_color]
            
            ballMap[ball] = color
            colorMap[color] = colorMap.get(color,0)+1
            res.append(len(colorMap))
        
        return res

        