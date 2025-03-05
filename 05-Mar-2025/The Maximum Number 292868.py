# Problem: The Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a = b=c = None
        for num in nums:
            if num in (a,b,c):
                continue
            if a is None or num > a:
                b,c,a = a,b,num
            elif b is None or num > b:
                b,c = num, b
            elif c is None or num > c:
                c = num
        return c if c is not None else a


        