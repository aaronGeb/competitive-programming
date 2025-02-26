# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        import numpy as np
        
        m, n = len(img), len(img[0])
        img = np.array(img, dtype=np.int32)
        result = np.zeros((m, n), dtype=np.int32)

        for i in range(m):
            for j in range(n):
                neighbors = img[max(0, i-1):min(m, i+2), max(0, j-1):min(n, j+2)]
                result[i, j] = np.sum(neighbors) // neighbors.size
        
        return result.tolist()


       



        

