# Problem: Remove Letter To Equalize Frequency - https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = Counter(word)
        keys = list(freq.keys())
        for char in keys:
            freq[char] -=1
            if freq[char] == 0:
                del freq[char]
            new_value =  list(freq.values())
            if len(set(new_value)) == 1:
                return True
            freq[char] +=1
        return False