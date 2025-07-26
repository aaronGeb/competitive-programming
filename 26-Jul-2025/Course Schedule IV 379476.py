# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
        
        prereq = defaultdict(set) 

        queue = deque()
        for i in range(numCourses):
            if not indegree[i]:
                queue.append(i) 

        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                for neigh in graph[node]:
                    prereq[neigh].add(node)
                    prereq[neigh].update(prereq[node])
 
                    indegree[neigh] -= 1
                    if not indegree[neigh]:
                        queue.append(neigh)
        
        result = [None] * len(queries)
        for i, (u, v) in enumerate(queries):
            result[i] = u in prereq[v] 
        
        return result
  