# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy  = ListNode()
        head = dummy
        left = list1
        right = list2
        while left and right:
            if left.val < right.val:
                head.next = ListNode(left.val)
                head  = head.next
                left = left.next
            else:
                head.next = ListNode(right.val)
                head  = head.next
                right = right.next
        while left:
            head.next = ListNode(left.val)
            head  = head.next
            left = left.next
        while right:
            head.next = ListNode(right.val)
            head  = head.next
            right = right.next
        return dummy.next


        