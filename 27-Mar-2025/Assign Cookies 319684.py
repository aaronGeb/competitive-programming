# Problem: Assign Cookies - https://leetcode.com/problems/assign-cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
    
        g_ptr, s_ptr = 0, 0
        content_children = 0
        while g_ptr < len(g) and s_ptr < len(s):
            if s[s_ptr] >= g[g_ptr]:
                content_children += 1
                g_ptr += 1
            s_ptr += 1
        return content_children