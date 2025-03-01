# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_one = 0
        max_row = 0
    
        for i,row in enumerate(mat):
            count_one = sum(row)
            if count_one > max_one:
                max_one =  count_one
                max_row = i
        return [max_row, max_one]

