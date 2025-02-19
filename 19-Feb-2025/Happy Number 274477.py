# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next_num(n):
            return sum(int(digit)**2 for digit in str(n))
        seen = set()
        while n!=1 and n not in seen:
            seen.add(n)
            n = get_next_num(n)
        return n==1

        