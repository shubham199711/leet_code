# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        running = head
        newHead = runningNew = None
        _sum = 0
        while running:
            if running.val == 0 and _sum != 0:
                if newHead is None:
                    newHead = runningNew = ListNode(_sum)
                else:
                    runningNew.next = ListNode(_sum)
                    runningNew = runningNew.next
                _sum = 0
            else:
                _sum += running.val
            running = running.next
        return newHead
        