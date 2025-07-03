# Problem: Pseudo-Palindromic Paths in a Binary Tree - https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/description/?envType=daily-question&envId=2024-01-24

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def dfs(node, path):
            if not node:
                return 0
            path ^= 1 << node.val
            
            if not node.left and not node.right:
                return int(path & (path - 1) == 0)
            return dfs(node.left, path) + dfs(node.right, path)
        
        return dfs(root, 0)