# Problem: Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None  
        return self._inorder_check(root)

    def _inorder_check(self, node: Optional[TreeNode]) -> bool:
        if not node:
            return True

        if not self._inorder_check(node.left):
            return False

        if self.prev is not None and node.val <= self.prev:
            return False

        self.prev = node.val

        return self._inorder_check(node.right)