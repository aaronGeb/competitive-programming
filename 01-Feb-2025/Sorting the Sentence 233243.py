# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        words.sort(key= lambda word: int (word[-1]))
        return ' '.join(w[:-1] for w in words)
        