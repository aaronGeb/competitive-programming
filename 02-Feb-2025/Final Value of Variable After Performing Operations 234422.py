# Problem: Final Value of Variable After Performing Operations - https://leetcode.com/problems/final-value-of-variable-after-performing-operations

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        n = len(operations)
        output = 0
        for i in operations:
            if i == '++X' or i == 'X++':
                output +=1
            elif i == '--X' or i== 'X--':
                output -= 1
        return output

        