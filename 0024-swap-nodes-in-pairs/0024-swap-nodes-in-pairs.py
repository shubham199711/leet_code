# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(0) # new head
        dummy.next, head = head, dummy
        while head.next and head.next.next:
            a, b = head.next, head.next.next
            head.next, a.next, b.next, head = b, b.next, a, a
        return dummy.next
            
        