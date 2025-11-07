# Problem: Copy List with Random Pointer - https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        node_map = {}
        dummy = tail = Node(0)

        cur = head
        while cur:
            clone = Node(cur.val)
            node_map[cur] = clone
            tail.next = clone
            tail = clone
            cur = cur.next
        cur = head
        while cur:
            node_map[cur].random = node_map.get(cur.random)
            cur = cur.next

        return dummy.next
        