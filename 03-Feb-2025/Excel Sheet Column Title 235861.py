# Problem: Excel Sheet Column Title - https://leetcode.com/problems/excel-sheet-column-title/description/?envType=problem-list-v2&envId=string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        column = []
        while columnNumber > 0:
            columnNumber -= 1
            value = chr(columnNumber%26 + ord('A'))
            column.append(value)
            columnNumber //=26
        return ''.join(column[::-1])

        