# Problem: Partition List - https://leetcode.com/problems/partition-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left  = ListNode()
        right = ListNode()
        left_ptr = left
        right_ptr = right
        while head:
            if head.val < x:
                left_ptr.next = head
                left_ptr = left_ptr.next
            else:
                right_ptr.next = head
                right_ptr = right_ptr.next
            head = head.next
        right_ptr.next = None
        left_ptr.next = right.next
        return left.next
