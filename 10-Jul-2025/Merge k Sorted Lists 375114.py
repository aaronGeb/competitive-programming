# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        heapq.heapify(heap)
        dummyNode = ListNode()
        head = dummyNode
    
        for index,node in enumerate(lists):
            if node:
                heapq.heappush(heap,(node.val,index))
            
        while heap:
            smallestElement,index = heapq.heappop(heap)
            currentElement = lists[index]
            head.next = currentElement
            head = currentElement
            nextNode = currentElement.next
            
            if nextNode:
                lists[index] = nextNode
                heapq.heappush(heap,(nextNode.val,index))
                
        return dummyNode.next
