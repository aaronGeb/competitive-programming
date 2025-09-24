# Problem: Ugly Number II - https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        seen = {1}
        primes = [2, 3, 5]

        for _ in range(n):
            ugly = heapq.heappop(heap)
            for p in primes:
                next_ugly = ugly * p
                if next_ugly not in seen:
                    seen.add(next_ugly)
                    heapq.heappush(heap, next_ugly)

        return ugly
