# Problem: Longest Turbulent Subarray - https://leetcode.com/problems/longest-turbulent-subarray/

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        n = len(arr)
        if n == 1:
            return 1

        max_length = 1
        left = 0

        for right in range(1, n):
            cmp = (arr[right - 1] > arr[right]) - (arr[right - 1] < arr[right])

            if cmp == 0:  # Reset if elements are equal
                left = right
            elif right == n - 1 or cmp * ((arr[right] > arr[right + 1]) - (arr[right] < arr[right + 1])) != -1:
                max_length = max(max_length, right - left + 1)
                left = right

        return max_length