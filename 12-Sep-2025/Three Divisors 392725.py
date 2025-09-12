# Problem: Three Divisors - https://leetcode.com/problems/three-divisors/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def isThree(self, n: int) -> bool:
        div  = set()
        for i in range(1, int(n**0.5)+1):
            if n %i ==0:
                div.add(i)
                div.add(n//i)
                if len(div) >3:
                    return False
        return True if len(div)==3 else False
        