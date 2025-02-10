# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            my_str = ''.join(sorted(s))
            if my_str in anagrams:
                anagrams[my_str].append(s)
            else:
                anagrams[my_str] = [s]
        return list(anagrams.values())
        