# Problem: Expression Add Operators - https://leetcode.com/problems/expression-add-operators/description/

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def backtrack(index, path, value, last):
            if index == len(num):
                if value == target:
                    result.append(path)
                return
            
            for i in range(index, len(num)):
                if i > index and num[index] == '0':
                    break  # avoid numbers with leading zero
                curr_str = num[index:i+1]
                curr_num = int(curr_str)
                
                if index == 0:
                    backtrack(i + 1, curr_str, curr_num, curr_num)
                else:
                    backtrack(i + 1, path + '+' + curr_str, value + curr_num, curr_num)
                    backtrack(i + 1, path + '-' + curr_str, value - curr_num, -curr_num)
                    backtrack(i + 1, path + '*' + curr_str, value - last + last * curr_num, last * curr_num)

        result = []
        backtrack(0, "", 0, 0)
        return result