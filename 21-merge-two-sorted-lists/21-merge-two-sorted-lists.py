# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from queue import PriorityQueue
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mainList = [list1, list2]
        queue = PriorityQueue()
        for item in mainList:
            while item is not None:
                queue.put((item.val, item.val))
                item = item.next
        running = head = None
        while not queue.empty():
            item = queue.get()[0]
            if head is None:
                head = running = ListNode(item)
            else:
                temp = ListNode(item)
                running.next = temp
                running = running.next
        return head
            
        