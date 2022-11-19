# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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
            
        
        
        