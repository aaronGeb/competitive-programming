# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        amot = [0] * (n+1)
        for i,k,j in shifts:
            d = 1 if j ==1 else -1
            amot[i] += d
            amot[k+1] -=d
        for idx in range(1,n):
            amot[idx] += amot[idx-1]
        
        r = []
        for it in range(n):
            net = (ord(s[it]) - ord('a') + amot[it]) % 26
            r.append(chr(ord('a') + net))
        return ''.join(r)

  
        