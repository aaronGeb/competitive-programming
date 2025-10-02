# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for (u, v), prob in zip(edges, succProb):
            graph[u].append((v, prob))
            graph[v].append((u, prob))
        
       
        max_heap = [(-1.0, start_node)]
        probs = [0.0] * n
        probs[start_node] = 1.0
        
        while max_heap:
            curr_prob, node = heapq.heappop(max_heap)
            curr_prob = -curr_prob
            
            if node == end_node:
                return curr_prob
            
            for nei, p in graph[node]:
                new_prob = curr_prob * p
                if new_prob > probs[nei]:
                    probs[nei] = new_prob
                    heapq.heappush(max_heap, (-new_prob, nei))
        
        return 0.0