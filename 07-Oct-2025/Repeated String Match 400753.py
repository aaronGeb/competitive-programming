# Problem: Repeated String Match - https://leetcode.com/problems/repeated-string-match/description/

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        ans = math.ceil(len(b) / len(a))
        repeated = a * ans
        if b in repeated:
            return ans
        if b in (repeated + a):
            return ans + 1
        return -1