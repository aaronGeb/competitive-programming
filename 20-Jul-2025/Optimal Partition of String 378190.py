# Problem: Optimal Partition of String - https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        count = 1

        for ch in s:
            if ch in seen:
                count += 1
                seen.clear()
            seen.add(ch)

        return count