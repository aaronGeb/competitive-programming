# Problem: Short Encoding of Words - https://leetcode.com/problems/short-encoding-of-words/

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = set(words)
        for w in list(words):
            for k in range(1, len(w)):
                words.discard(w[k:])
        return sum(len(w) + 1 for w in words)