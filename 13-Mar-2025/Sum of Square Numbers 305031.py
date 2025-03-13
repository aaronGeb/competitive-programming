# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(math.sqrt(c))
        while a<=b:
            ab_sum = a**2 + b**2
            if ab_sum == c:
                return True
            elif ab_sum <c:
                a +=1
            else:
                b = b-1
        return False