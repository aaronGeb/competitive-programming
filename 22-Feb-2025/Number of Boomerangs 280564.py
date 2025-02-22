# Problem: Number of Boomerangs - https://leetcode.com/problems/number-of-boomerangs/description/

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        count = 0

        for i in range(n):
            distances = {}  # Dictionary to store distances from point i

            for j in range(n):
                if i != j:
                    distance = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                    distances[distance] = distances.get(distance, 0) + 1

            for distance_count in distances.values():
                count += distance_count * (distance_count - 1)

        return count
