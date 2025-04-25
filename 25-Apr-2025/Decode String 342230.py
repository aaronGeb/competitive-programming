# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        string = ""

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == "[":
                stack.append((string, num))
                string = ""
                num = 0
            elif ch == "]":
                prev_string, repeat = stack.pop()
                string = prev_string + string * repeat
            else:
                string += ch

        return string
            