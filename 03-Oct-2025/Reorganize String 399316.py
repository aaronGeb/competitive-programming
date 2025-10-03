# Problem: Reorganize String - https://leetcode.com/problems/reorganize-string/description/

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        if max(freq.values()) > (len(s) + 1) // 2:
            return ""
        heap = [(-cnt, ch) for ch, cnt in freq.items()]
        heapq.heapify(heap)
        
        result = []
        
        while len(heap) >= 2:
        
            cnt1, ch1 = heapq.heappop(heap)
            cnt2, ch2 = heapq.heappop(heap)
            
            result.extend([ch1, ch2])
            
            if cnt1 + 1 < 0:
                heapq.heappush(heap, (cnt1 + 1, ch1))
            if cnt2 + 1 < 0:
                heapq.heappush(heap, (cnt2 + 1, ch2))
        
        if heap:
            result.append(heap[0][1])
        
        return "".join(result)
