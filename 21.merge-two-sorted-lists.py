# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from queue import PriorityQueue
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prorityQueue = PriorityQueue()
        _lists = [list1, list2]
        for _list in _lists:
            while _list is not None:
                prorityQueue.put((_list.val,_list.val))
                _list = _list.next
        head = running = None
        while not prorityQueue.empty():
            item = prorityQueue.get()[1]
            if head is None:
                head = running = ListNode(item)
            else:
                temp = ListNode(item)
                running.next = temp
                running = running.next
        return head