# Problem: Sort Items by Groups Respecting Dependencies - https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        for i in range(n):
            if group[i] == -1:
             group[i] = m
            m += 1
        item_graph = defaultdict(list)
        item_indegree = [0] * n
        group_graph = defaultdict(list)
        group_indegree = [0] * m

        for v in range(n):
            for u in beforeItems[v]:
                item_graph[u].append(v)
                item_indegree[v] += 1
                if group[u] != group[v]:  
                    group_graph[group[u]].append(group[v])
                    group_indegree[group[v]] += 1

        def topo_sort(graph, indegree, nodes):
            q = deque([x for x in nodes if indegree[x] == 0])
            res = []
            while q:
                u = q.popleft()
                res.append(u)
                for v in graph[u]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        q.append(v)
            return res if len(res) == len(nodes) else []

        item_order = topo_sort(item_graph, item_indegree, range(n))
        group_order = topo_sort(group_graph, group_indegree, range(m))
        if not item_order or not group_order:
            return []

        order_map = defaultdict(list)
        for item in item_order:
            order_map[group[item]].append(item)

        res = []
        for g in group_order:
            res.extend(order_map[g])
        return res