# Problem: 2096. Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/?envType=problem-list-v2&envId=depth-first-search

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(node, val, path):
            if not node:
                return False
            if node.val == val:
                return True
            path.append('L')
            if dfs(node.left, val, path):
                return True
            path.pop()
            path.append('R')
            if dfs(node.right, val, path):
                return True
            path.pop()
            return False

        pathToStart, pathToDest = [], []
        dfs(root, startValue, pathToStart)
        dfs(root, destValue, pathToDest)

        i = 0
        while i < len(pathToStart) and i < len(pathToDest) and pathToStart[i] == pathToDest[i]:
            i += 1

        return 'U' * (len(pathToStart) - i) + ''.join(pathToDest[i:])