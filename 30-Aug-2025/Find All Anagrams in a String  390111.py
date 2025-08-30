# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
       
        n, m = len(s), len(p)
        if m > n:
            return result
        
        p_count = Counter(p)
        s_count = Counter(s[:m])
        
        if s_count == p_count:
            result.append(0)
        
        for i in range(m, n):
            s_count[s[i]] += 1
            s_count[s[i - m]] -= 1
            
            if s_count[s[i - m]] == 0:
                del s_count[s[i - m]]
            
            if s_count == p_count:
                result.append(i - m + 1)
        
        return result