# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        
        digits = sorted(str(abs(num)))
        if num > 0:
            if digits[0] == '0':
                first_non_zero = next(i for i in range(len(digits)) if digits[i] != '0')
                digits[0], digits[first_non_zero] = digits[first_non_zero], digits[0]
        else:
            digits.reverse()
        
        return int(''.join(digits)) * (-1 if num < 0 else 1)



        