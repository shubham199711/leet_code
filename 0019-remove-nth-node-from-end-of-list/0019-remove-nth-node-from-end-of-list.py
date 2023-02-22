# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        front, tail = head, head
        if not front:
            return head
        for _ in range(n):
            front = front.next
        while front and front.next:
            front = front.next
            tail = tail.next
        if front:
            tail.next = tail.next.next
        else:
            head = head.next
        return head
        