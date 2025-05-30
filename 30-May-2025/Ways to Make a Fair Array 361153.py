# Problem: Ways to Make a Fair Array - https://leetcode.com/problems/ways-to-make-a-fair-array/description/

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        sum_even = sum(nums[i] for i in range(n) if i %2==0)
        sum_odd = sum(nums[i] for i in range(n) if i%2==1)

        result = 0
        even = 0
        odd = 0

        for i in range(n):
            if i % 2 == 0:
                sum_even -= nums[i]
            else:
                sum_odd -= nums[i]

            if even + sum_odd == odd + sum_even:
                result += 1

            if i % 2 == 0:
                even += nums[i]
            else:
                odd += nums[i]

        return result