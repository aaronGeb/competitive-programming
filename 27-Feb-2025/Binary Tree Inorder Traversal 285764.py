# Problem: Binary Tree Inorder Traversal - https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        my_result = []
        def inorder_traverse(node):
            if not node:
                return 
            inorder_traverse(node.left)
            my_result.append(node.val)
            inorder_traverse(node.right)
        inorder_traverse(root)
        return my_result
        