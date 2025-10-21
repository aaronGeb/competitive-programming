# Problem: Reverse String - https://leetcode.com/problems/reverse-string/description/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        right = len(s) - 1
        for left in range(len(s) // 2):
            s[left], s[right] = s[right], s[left]
            right -= 1

        