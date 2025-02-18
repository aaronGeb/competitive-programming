# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        idx = 0
        while i < len(chars):
            char = chars[i]
            count = 0
            while i < len(chars) and chars[i] == char:
                count +=1
                i +=1
            chars[idx] = char
            idx +=1
            if count >1:
                for digit in str(count):
                    chars[idx] = digit
                    idx +=1
        return idx
        