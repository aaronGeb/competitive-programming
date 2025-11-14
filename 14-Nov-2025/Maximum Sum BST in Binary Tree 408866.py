# Problem: Maximum Sum BST in Binary Tree - https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        
        self.best = 0

        def dfs(node):
            if not node:
                return True, float('inf'), float('-inf'), 0

            left_ok, left_min, left_max, left_sum = dfs(node.left)
            right_ok, right_min, right_max, right_sum = dfs(node.right)

            if left_ok and right_ok and left_max < node.val < right_min:
                total = left_sum + right_sum + node.val
                self.best = max(self.best, total)
                return True, min(left_min, node.val), max(right_max, node.val), total

            return False, 0, 0, 0

        dfs(root)
        return self.best
        