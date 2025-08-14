# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        @cache
        def dfs(i):
            if i >= n:
                return 0
            points, brainpower = questions[i]
            solve = points + dfs(i + brainpower + 1)
            skip = dfs(i + 1)
            return max(solve, skip)

        return dfs(0)