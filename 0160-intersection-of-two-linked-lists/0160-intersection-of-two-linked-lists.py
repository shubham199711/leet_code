# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = {}
        a, b = headA, headB
        while a:
            seen[a] = True
            a = a.next
        while b:
            if seen.get(b) is not None:
                return b
            b = b.next
        return None
        