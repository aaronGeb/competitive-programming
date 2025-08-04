# Problem: 2115. Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree = defaultdict(int)
        graph = defaultdict(list)
        for i, recipe in enumerate(recipes):
            for ing in ingredients[i]:
                graph[ing].append(recipe)
                indegree[recipe] += 1
        queue = deque(supplies)
        available = set(supplies)
        result = []

        while queue:
            item = queue.popleft()

            for recipe in graph[item]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    queue.append(recipe)
                    result.append(recipe)
                    available.add(recipe)

        return result