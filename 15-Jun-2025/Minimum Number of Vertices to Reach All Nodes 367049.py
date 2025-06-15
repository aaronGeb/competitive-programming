# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree = set(range(n))
    
        for u, v in edges:
            if v in in_degree:
                in_degree.remove(v)
        
        return list(in_degree)