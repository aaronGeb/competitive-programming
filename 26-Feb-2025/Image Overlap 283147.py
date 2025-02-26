# Problem: Image Overlap - https://leetcode.com/problems/image-overlap/description/

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        max_overlap = 0
        for dx in range(-n+1, n):
            for dy in range(-n+1,n):
                overlap =0
                for i in range(n):
                    for j in range(n):
                        x =  i + dx
                        y = j+ dy
                        if 0<=x<n and 0<=y<n:
                            if img1[i][j]== 1 and img2[x][y]==1:
                                overlap +=1
                if overlap > max_overlap:
                    max_overlap = overlap
        return max_overlap

    
        