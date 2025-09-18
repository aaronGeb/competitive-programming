# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1== s2:
            return  True
        diffrence = [(i,j) for i,j in zip(s1,s2) if i !=j]
        return len(diffrence) ==2 and diffrence[0]== diffrence[1][::-1]