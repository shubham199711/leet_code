# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        running = head
        prev = None
        while running:
            if running.val == val:
                if prev:
                    prev.next = running.next
                else:
                    head = head.next
            else:
                prev = running
            running = running.next
        return head