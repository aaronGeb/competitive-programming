# Problem: Kth Symbol in Grammer - https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        parent = self.kthGrammar(n - 1, math.ceil(k / 2))

        if k % 2 == 1:
            return parent
        else:
            return 1 - parent
        