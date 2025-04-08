# Problem: Number of Substrings Containing All Three Characters - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        count = defaultdict(int)
        res = 0
        left = 0
        

        for right in range(len(s)):
            count[s[right]] += 1

            while all(count[c] > 0 for c in "abc"):
                res += len(s) - right
                count[s[left]] -= 1
                left += 1

        return res
        