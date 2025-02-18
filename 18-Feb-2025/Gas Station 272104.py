# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        current_gas = 0
        start_index = 0
        n = len(gas)
        for i in range(n):
            balance = gas[i] - cost[i]
            total_gas += balance
            current_gas += balance
            if current_gas < 0:
                start_index = i+1
                current_gas = 0
        return start_index if total_gas >= 0 else -1
