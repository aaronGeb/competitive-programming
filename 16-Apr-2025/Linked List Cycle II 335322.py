# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """#
        h = {}
        while head and head.next:
            if head.val in h and head.next.val == h[head.val]:
                return head
            h[head.val] = head.next.val

            head = head.next
        return None"""
        slow = fast = head
        flag = False
        # phase 1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                flag = True
                break
        if not flag:
            return None
        
                
        # pahse 2
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow


        