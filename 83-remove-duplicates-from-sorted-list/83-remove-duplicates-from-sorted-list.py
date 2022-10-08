# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        seen = set()
        newHead = front = None
        runningHead = head
        while runningHead is not None:
            if runningHead.val in seen:
                runningHead = runningHead.next
                continue
            seen.add(runningHead.val)
            if newHead is None:
                newHead = front = ListNode(runningHead.val)
            else:
                newHead.next = ListNode(runningHead.val)
                newHead = newHead.next
            runningHead = runningHead.next
        return front
        