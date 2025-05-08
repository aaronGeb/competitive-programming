# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        n = len(arr)
        stack = []
        prev_less = [0] * n
        next_less = [0] * n

        # Previous Less Element
        for i in range(n):
            count = 1
            while stack and stack[-1][0] > arr[i]:
                count += stack.pop()[1]
            prev_less[i] = count
            stack.append((arr[i], count))

        stack = []

        # Next Less Element
        for i in range(n - 1, -1, -1):
            count = 1
            while stack and stack[-1][0] >= arr[i]:
                count += stack.pop()[1]
            next_less[i] = count
            stack.append((arr[i], count))

        result = 0
        for i in range(n):
            result += arr[i] * prev_less[i] * next_less[i]
            result %= mod

        return result