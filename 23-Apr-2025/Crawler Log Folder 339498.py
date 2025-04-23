# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        result = 0
        for log in logs:
            if log == "../":
                result = max(0, result - 1)
            elif log[0] != ".":
                result += 1
        return result