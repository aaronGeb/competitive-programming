# Problem: Walking Robot Simulation - https://leetcode.com/problems/walking-robot-simulation/description/?envType=problem-list-v2&envId=array

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = deque([(0, 1), (1, 0), (0, -1), (-1, 0)])
        direction_idx  = 0
        x, y = 0, 0 
        max_distance_sq = 0 
        obstacle_set = set(map(tuple, obstacles))
        for cmd in commands:
            if cmd == -2:
                direction_idx = (direction_idx - 1) % 4
            elif cmd == -1:  
                direction_idx = (direction_idx + 1) % 4
            else:  
                dx, dy = directions[direction_idx]  
                for _ in range(cmd):  
                    if (x + dx, y + dy) in obstacle_set:
                        break  
                    x += dx
                    y += dy
                    max_distance_sq = max(max_distance_sq, x**2 + y**2)

        return max_distance_sq
