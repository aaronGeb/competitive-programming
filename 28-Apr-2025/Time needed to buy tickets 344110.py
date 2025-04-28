# Problem: Time needed to buy tickets - https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        for i, val in enumerate(tickets):
            time += min(val, tickets[k] if i <= k else tickets[k] - 1)
        return time
        