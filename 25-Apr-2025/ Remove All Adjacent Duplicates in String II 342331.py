# Problem:  Remove All Adjacent Duplicates in String II - https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        result = []
        for char in s:
            result.append(char)
            if len(result)>= k and [char]*k == result[-k:]:
                del result[-k:]
        return ''.join(result)