# Problem: Partition String  - https://leetcode.com/problems/partition-string/description/

class Solution:
    def partitionString(self, s: str) -> List[str]:
        visit = set()
        result = []
        ans = ""
        for char in s:
            ans += char
            if ans not in visit:
                visit.add(ans)
                result.append(ans)
                ans = ""
        return result

        