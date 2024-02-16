# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t1, t2, t3, head, carry = l1, l2, None, None, 0
        while t1 or t2:
            a1, a2 = 0 , 0
            if t1:
                a1 = t1.val
                t1 = t1.next
            if t2:
                a2 = t2.val
                t2 = t2.next
            _sum = int(a1) + int(a2) + carry
            if _sum > 9:
                carry = 1
                _sum = int(str(_sum)[-1])
            else:
                carry = 0
            if head is None:
                head = t3 = ListNode(_sum)
            else:
                t3.next = ListNode(_sum)
                t3 = t3.next
        if carry:
            t3.next = ListNode(1)
            t3 = t3.next
        return head
        