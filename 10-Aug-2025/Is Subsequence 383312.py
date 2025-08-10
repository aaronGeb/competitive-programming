# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer_s, pointer_t = 0, 0
        len_s, len_t = len(s), len(t)

        while pointer_s < len_s and pointer_t < len_t:
          if s[pointer_s] == t[pointer_t]:
            pointer_s += 1
          pointer_t += 1
        return pointer_s == len_s

        