# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        max_count = 0
        char_count = {}
        left = 0

        for right, char in enumerate(s):
            char_count[char] = char_count.get(char, 0) + 1
            max_count = max(max_count, char_count[char])
            while right - left + 1 - max_count > k:
                char_count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length

        
        