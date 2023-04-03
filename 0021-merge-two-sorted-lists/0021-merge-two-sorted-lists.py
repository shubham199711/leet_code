# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from queue import PriorityQueue
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = head = ListNode(None)
        while list1 and list2:
                if list1.val < list2.val:
                    newHead.next = ListNode(list1.val)
                    newHead = newHead.next
                    list1 = list1.next
                else:
                    newHead.next = ListNode(list2.val)
                    newHead = newHead.next
                    list2 = list2.next
        while list1:
            newHead.next = ListNode(list1.val)
            newHead = newHead.next
            list1 = list1.next
        while list2:
            newHead.next = ListNode(list2.val)
            newHead = newHead.next
            list2 = list2.next
        return head.next