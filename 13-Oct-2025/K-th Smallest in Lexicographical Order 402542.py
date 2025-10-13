# Problem: K-th Smallest in Lexicographical Order - https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k -= 1  

        while k > 0:
            count = self.get_count(curr, n)
            if k >= count:
                k -= count
                curr += 1
            else:
                k -= 1
                curr *= 10

        return curr

    def get_count(self, prefix: int, n: int) -> int:
        count = 0
        curr, next_prefix = prefix, prefix + 1
        while curr <= n:
            count += min(n + 1, next_prefix) - curr
            curr *= 10
            next_prefix *= 10
        return count