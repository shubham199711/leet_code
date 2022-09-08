# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode_my(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return -1
        temp = head
        _ans = []
        while temp:
            _ans.append(temp)
            temp = temp.next
        return _ans[len(_ans) // 2]

    
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow