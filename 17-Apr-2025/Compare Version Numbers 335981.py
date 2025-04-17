# Problem: Compare Version Numbers - https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        max_len = max(len(v1), len(v2))
        for i in range(max_len):
            n = int(v1[i]) if i < len(v1) else 0
            m = int(v2[i]) if i < len(v2) else 0
            if n > m:
                return 1
            elif n< m:
                return -1
        return 0
        