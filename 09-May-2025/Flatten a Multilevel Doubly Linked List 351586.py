# Problem: Flatten a Multilevel Doubly Linked List - https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/?envType=problem-list-v2&envId=linked-list

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        def dfs(prev, node):
            if not node:
                return prev
            node.prev = prev
            prev.next = node

            next_node = node.next
            tail = dfs(node, node.child)
            node.child = None
            return dfs(tail, next_node)

        dummy = Node(0, None, head, None)
        dfs(dummy, head)
        head.prev = None
        return head
        