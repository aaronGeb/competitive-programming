# Problem: Reverse Words in a String - https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        n = len(words)
        for i in range(n//2):
            words[i],words[n-i-1] = words[n-i-1], words[i]
        return ' '.join(words)


        