# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0
        d = 2
        while d * d <= n:
            while n % d == 0:
                ans += d
                n //= d
            d += 1
        if n > 1:
            ans += n
        return ans