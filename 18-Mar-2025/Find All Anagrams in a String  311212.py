# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        pmap = Counter(p)
        n = len(p)
        for i in range(0,len(s)-n+1,1):
            smap = Counter(s[i:i+n])
            if pmap == smap:
                result.append(i)
        return result
        