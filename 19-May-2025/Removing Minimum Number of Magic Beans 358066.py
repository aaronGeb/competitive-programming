# Problem: Removing Minimum Number of Magic Beans - https://leetcode.com/problems/removing-minimum-number-of-magic-beans/

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        s = sum(beans)
        n =  len(beans)
        return min(s - x * (n - i) for i, x in enumerate(beans))