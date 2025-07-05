# Problem: Count Vowel Strings in Ranges - https://leetcode.com/problems/count-vowel-strings-in-ranges/

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def is_vowel(ch):
            return ch in 'aeiou'

        def is_vowel_string(word):
            return is_vowel(word[0]) and is_vowel(word[-1])

        pre = [0]
        for word in words:
            pre.append(pre[-1] + (1 if is_vowel_string(word) else 0))

        return [pre[r+1] - pre[l] for l, r in queries]