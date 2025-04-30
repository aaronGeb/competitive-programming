# Problem: Super Pow - https://leetcode.com/problems/super-pow/description/

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        mod = 1337
        ans  = ''
        result =0
        for e in b:
            ans += str(e) 
            result = pow(a, int(ans), mod)
        return result
        