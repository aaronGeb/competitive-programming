# Problem: Minimum Number of Days to Make m Bouquets - https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m *k > n:
            return -1
        def buildbouquets(day):
            bouq = 0
            flower = 0
            for i in range(n):
                if bloomDay[i] <= day:
                    flower +=1
                    if flower == k:
                        bouq +=1
                        flower = 0
                else:
                    flower = 0
            return bouq
        l = min(bloomDay)
        r = max(bloomDay)
        result = 0
        while l<=r:
            mid = (l+r)//2
            if buildbouquets(mid) >= m:
                result = mid
                r = mid -1
            else:
                l = mid +1
        return result