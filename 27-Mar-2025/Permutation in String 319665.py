# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        s1_count = Counter(s1)
        windo_count =  Counter(s2[:n1])
        if s1_count == windo_count:
            return True
        # sliding windo
        for i in range(n1, n2):
            windo_count[s2[i]] +=1
            windo_count[s2[i- n1]] -=1
            if windo_count[s2[i-n1]] == 0:
                del windo_count[s2[i-n1]]
            if windo_count == s1_count:
                return True
        return False
       