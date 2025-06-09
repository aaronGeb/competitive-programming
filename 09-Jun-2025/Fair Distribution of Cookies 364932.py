# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        dist = [0] * k
        self.ans = float('inf')

        def backtrack(i):
            if i == len(cookies):
                self.ans = min(self.ans, max(dist))
                return
            
            for j in range(k):
                dist[j] += cookies[i]
                if dist[j] < self.ans:
                    backtrack(i + 1)
                dist[j] -= cookies[i]
                if dist[j] == 0:
                    break

        backtrack(0)
        return self.ans