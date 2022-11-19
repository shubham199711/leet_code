# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans1, ans2 = [], []
        t1, t2 = l1, l2
        while t1 or t2:
            if t1:
                ans1.append(str(t1.val))
                t1 = t1.next
            if t2:
                ans2.append(str(t2.val))
                t2 = t2.next
        ans1 = int(''.join(ans1[::-1]))
        ans2 = int(''.join(ans2[::-1]))
        ans = str(ans1 + ans2)
        head = temp = None
        for item in ans[::-1]:
            if not head:
                head = temp = ListNode(int(item))
            else:
                temp.next = ListNode(int(item))
                temp = temp.next
        return head
            
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t1, t2, t3, head, curry = l1, l2, None, None, 0
        while t1 or t2:
            ans1, ans2 = 0, 0
            if t1:
                ans1 = t1.val
                t1 = t1.next
            if t2:
                ans2 = t2.val
                t2 = t2.next
            ans = ans1 + ans2 + curry
            if ans > 9:
                curry = 1
                ans = int(str(ans)[-1])
            else:
                curry = 0
            if not head:
                head = temp = ListNode(ans)
            else:
                temp.next = ListNode(ans)
                temp = temp.next
        if curry:
            temp.next = ListNode(1)
            temp = temp.next
        return head
        