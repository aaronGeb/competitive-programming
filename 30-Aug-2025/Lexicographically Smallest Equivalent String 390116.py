# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        parent = list(range(26))  
        for a, b in zip(s1, s2):
            x, y = ord(a) - ord("a"), ord(b) - ord("a")
            px, py = find(x), find(y)
            if px < py:
                parent[py] = px  
            else:
                parent[px] = py  
        return "".join(
            chr(find(ord(c) - ord("a")) + ord("a")) for c in baseStr)