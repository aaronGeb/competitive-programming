from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_t = Counter(t)
        count_s = Counter(s)
        return count_t == count_s
