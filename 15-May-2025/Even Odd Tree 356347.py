# Problem: Even Odd Tree - https://leetcode.com/problems/even-odd-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level_vals = defaultdict(list)

        def dfs(node, level):
            if not node:
                return
            level_vals[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        for level, vals in level_vals.items():
            if level % 2 == 0:
                if any(v % 2 == 0 for v in vals) or any(vals[i] >= vals[i + 1] for i in range(len(vals) - 1)):
                    return False
            else:
                if any(v % 2 == 1 for v in vals) or any(vals[i] <= vals[i + 1] for i in range(len(vals) - 1)):
                    return False

        return True