# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        flag = False
        new_line = []
        for line in source:
            i = 0
            while i <len(line):
                if not flag and i+1 < len(line) and line[i] =='/' and line[i+1]=='*':
                    flag = True
                    i +=1
                elif flag and i+1 < len(line) and line[i] == '*' and line[i+1]=='/':
                    flag = False
                    i +=1
                elif not flag and i+1 < len(line) and line[i] == '/' and line[i+1]=='/':
                    break
                elif not flag:
                    new_line.append(line[i])
                i +=1
            if not flag and new_line:
                result.append(''.join(new_line))
                new_line = []
        return result