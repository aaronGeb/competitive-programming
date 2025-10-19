# Problem: Find Beautiful Indices in the Given Array I - https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/description/

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        a_indices = []
        b_indices = []
        start = 0
        while True:
            i = s.find(a, start)
            if i == -1:
                break
            a_indices.append(i)
            start = i + 1
        start = 0
        while True:
            j = s.find(b, start)
            if j == -1:
                break
            b_indices.append(j)
            start = j + 1

        res = []
        for i in a_indices:
            pos = bisect.bisect_left(b_indices, i)
            ok = False
            if pos < len(b_indices) and abs(b_indices[pos] - i) <= k:
                ok = True
            if pos > 0 and abs(b_indices[pos - 1] - i) <= k:
                ok = True
            if ok:
                res.append(i)

        return res
