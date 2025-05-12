# Problem: Heaters - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        def is_covered(radius: int) -> bool:
            i = j = 0
            while i < len(houses):
                if j == len(heaters):
                    return False
                left, right = heaters[j] - radius, heaters[j] + radius
                if houses[i] < left:
                    return False
                elif houses[i] > right:
                    j += 1
                else:
                    i += 1
            return True

        left, right = 0, 10**9
        while left < right:
            mid = (left + right) // 2
            if is_covered(mid):
                right = mid
            else:
                left = mid + 1

        return left