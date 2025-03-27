# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count_white = blocks[:k].count('W')
        min_recoloring = count_white
        for i in range(k,len(blocks)):
            if blocks[i-k] == 'W':
                count_white -= 1
            if blocks[i] == 'W':
                count_white +=1
            min_recoloring = min(min_recoloring, count_white)
        return min_recoloring
        