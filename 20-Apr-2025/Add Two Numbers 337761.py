# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current = ListNode(0)
        prev = current
        carry = 0

        while l1 is not None or l2 is not None or carry == 1:
            total = 0
            if l1 is not None:
                total += l1.val
                l1 = l1.next
            if l2 is not None:
                total += l2.val
                l2 = l2.next

            total += carry
            carry = total // 10
            mod = total % 10
            node = ListNode(mod)
            prev.next = node
            prev = prev.next

        return current.next
        