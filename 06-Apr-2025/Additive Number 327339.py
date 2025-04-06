# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        
        for i in range(1, n):  # i = length of first number
            for j in range(i + 1, n):  # j = length of second number
                num1 = num[:i]
                num2 = num[i:j]

                # Skip if either number has leading zero
                if (len(num1) > 1 and num1[0] == '0') or (len(num2) > 1 and num2[0] == '0'):
                    continue
                
                a, b = int(num1), int(num2)
                k = j
                while k < n:
                    c = a + b
                    c_str = str(c)
                    if not num.startswith(c_str, k):
                        break
                    k += len(c_str)
                    a, b = b, c
                
                if k == n:
                    return True
        
        return False

        