# Problem: Rotate List - https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        size = 1
        tail = head
        while tail.next:
            tail =  tail.next
            size +=1
        k = k% size
        if k ==0:
            return head
        current = head
        for _ in range(size -k -1):
            current = current.next
        dummyHead = current.next
        current.next =  None
        tail.next = head
        return dummyHead

        