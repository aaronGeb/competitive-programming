# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = ['']* len(s)
        for i,char in enumerate(s):
            result[indices[i]] = char
        return ''.join(result)
        