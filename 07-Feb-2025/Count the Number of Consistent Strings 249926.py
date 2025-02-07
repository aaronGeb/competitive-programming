# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        my_uniq = set(allowed)
        count = 0
        for word in words:
            if all(char in my_uniq for char in word):
                count +=1
        return count
        