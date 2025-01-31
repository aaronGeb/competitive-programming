# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_count = Counter(words[0])
        for word in  words[1:]:
            common_count &= Counter(word)
        result = []
        for ch,frq in common_count.items():
            result.extend([ch]*frq)
        return result     