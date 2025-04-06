# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need = Counter(t)
        window = {}
        
        have, need_count = 0, len(need)
        res, res_len = [-1, -1], float("inf")
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                have += 1

            while have == need_count:
                # Update result
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # Pop from the left
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""

        