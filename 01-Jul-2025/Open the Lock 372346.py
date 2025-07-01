# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        visited = set()
        start = "0000"

        if start in dead:
            return -1

        queue = deque([(start, 0)])  
        visited.add(start)

        while queue:
            state, depth = queue.popleft()

            if state == target:
                return depth

            for i in range(4):
                digit = int(state[i])
                for move in [-1, 1]:
                    new_digit = (digit + move) % 10
                    new_state = state[:i] + str(new_digit) + state[i+1:]
                    if new_state not in dead and new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, depth + 1))

        return -1
