# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        parent = list(range(26))  
        for equation in equations:
            a, b = ord(equation[0]) - ord('a'), ord(equation[-1]) - ord('a')
            if equation[1] == '=':
                parent[find(a)] = find(b)
        for equation in equations:
            a, b = ord(equation[0]) - ord('a'), ord(equation[-1]) - ord('a')
            if equation[1] == '!' and find(a) == find(b):
                return False
        
        return True