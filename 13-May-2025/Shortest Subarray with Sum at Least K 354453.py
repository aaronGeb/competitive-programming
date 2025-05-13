# Problem: Shortest Subarray with Sum at Least K - https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        dq = deque()
        res = n + 1

        for i in range(n + 1):
            while dq and prefix[i] - prefix[dq[0]] >= k:
                res = min(res, i - dq.popleft())

            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()

            dq.append(i)

        return res if res <= n else -1