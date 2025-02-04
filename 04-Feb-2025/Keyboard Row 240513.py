# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row_1 = set('qwertyuiop')
        row_2 = set('asdfghjkl')
        row_3 = set('zxcvbnm')
        def is_single_row(word):
            lower_word =  set(word.lower())
            return lower_word <= row_1 or lower_word <= row_2 or lower_word <= row_3
        return [word for word in words if is_single_row(word)]

        