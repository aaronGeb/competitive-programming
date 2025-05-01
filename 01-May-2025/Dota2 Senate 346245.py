# Problem: Dota2 Senate - https://leetcode.com/problems/dota2-senate/

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queu_r = deque()
        queu_d = deque()
        for i, c in enumerate(senate):
            if c == "R":
                queu_r.append(i)
            else:
                queu_d.append(i)
        n = len(senate)
        while queu_r and queu_d:
            if queu_r[0] < queu_d[0]:
                queu_r.append(queu_r[0] + n)
            else:
                queu_d.append(queu_d[0] + n)
            queu_r.popleft()
            queu_d.popleft()
        return "Radiant" if queu_r else "Dire"