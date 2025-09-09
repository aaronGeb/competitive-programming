# Problem: Number of Nodes in the Sub-Tree With the Same Label - https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        ans = [0] * n

        def dfs(node, parent):
            count = Counter()
            count[labels[node]] += 1
            for child in graph[node]:
                if child == parent:
                    continue
                child_count = dfs(child, node)
                count += child_count
            ans[node] = count[labels[node]]
            return count

        dfs(0, -1)
        return ans