# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from queue import PriorityQueue
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1, head2 = list1, list2
        newHead = running = ListNode(None)
        while head1 and head2:
            if head1.val < head2.val:
                running.next = ListNode(head1.val)
                running = running.next
                head1 = head1.next
            else:
                running.next = ListNode(head2.val)
                running = running.next
                head2 = head2.next
        while head1:
            running.next = ListNode(head1.val)
            running = running.next
            head1 = head1.next
        while head2:
            running.next = ListNode(head2.val)
            running = running.next
            head2 = head2.next
        return newHead.next