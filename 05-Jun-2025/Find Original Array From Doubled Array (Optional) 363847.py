# Problem: Find Original Array From Doubled Array (Optional) - https://leetcode.com/problems/find-original-array-from-doubled-array/

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []

        count = Counter(changed)
        changed.sort()
        original = []

        for x in changed:
            if count[x] == 0:
                continue
            if count[2 * x] == 0:
                return []
            original.append(x)
            count[x] -= 1
            count[2 * x] -= 1

        return original