# Problem: Count Vowel Substrings of a String - https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        n = len(word)
        for i in range(n):
            for j in range(i + 1, n + 1):
                substring = word[i:j]
                if all(c in vowels for c in substring):
                    if {'a', 'e', 'i', 'o', 'u'}.issubset(set(substring)):
                        count += 1
        return count
      



        