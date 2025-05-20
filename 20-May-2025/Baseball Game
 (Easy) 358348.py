# Problem: Baseball Game
 (Easy) - https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        myList = []
        for i in  operations:
            if i == '+':
                myList.append(myList[-1] +myList[-2])
            elif i == 'D':
                myList.append(2 * myList[-1])
            elif i == 'C':
                myList.pop()
            else:
                myList.append(int(i))
        return sum(myList)