# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        prev = head
        current = head
        for _ in range(n):
            current = current.next
            if not current:
                return head.next
        while current.next:
            current = current.next
            prev = prev.next
        prev.next = prev.next.next
        return head 
        
       
        