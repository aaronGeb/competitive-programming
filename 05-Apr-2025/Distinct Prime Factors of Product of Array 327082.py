# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            d = 2
            while d*d <= num:
                while num%d==0:
                    s.add(d)
                    num = num//d
                d +=1
            if num >1:
                s.add(num)
        return len(s)

        