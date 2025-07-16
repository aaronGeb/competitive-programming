# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        nfive = nten = 0

        for bill in bills:
            if bill == 5:
                nfive += 1
            elif bill == 10:
                if nfive == 0:
                    return False
                nfive -= 1
                nten += 1
            else:
                if nten > 0 and nfive > 0:
                    nten -= 1
                    nfive -= 1
                elif nfive >= 3:
                    nfive -= 3
                else:
                    return False

        return True