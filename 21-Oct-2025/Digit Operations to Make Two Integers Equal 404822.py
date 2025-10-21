# Problem: Digit Operations to Make Two Integers Equal - https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minOperations(self, n: int, m: int) -> int:
        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, int(x**0.5)+1):
                if x % i == 0:
                    return False
            return True
            
        def helper(curr):
            neighbors = []
            s = str(curr)
            for i in range(len(s)):
                d = int(s[i])
                if d != 9:
                    next = int(s[:i] + str(d+1) + s[i+1:])
                    if next != 0 and next not in visited and not is_prime(next):
                        neighbors.append(next)
                if d != 0:
                    next = int(s[:i] + str(d-1) + s[i+1:])
                    if next != 0 and next not in visited and not is_prime(next):
                        neighbors.append(next)
            return neighbors
            
        if is_prime(n):
            return -1

        q, visited = [(n,n)], {}
        while q:
            cost, curr = heapq.heappop(q)
            if curr == m:
                return cost
            if curr in visited and visited[curr] <= cost:
                continue 
            visited[curr] = cost
            for neighbor in helper(curr):
                if not is_prime(neighbor):
                    heapq.heappush(q,(cost+neighbor, neighbor))

        return -1            