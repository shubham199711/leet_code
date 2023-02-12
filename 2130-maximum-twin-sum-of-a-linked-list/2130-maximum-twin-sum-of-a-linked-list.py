# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        _list = []
        _ans = 0
        root = head
        while root:
            _list.append(root.val)
            root = root.next
        for i in range(len(_list) // 2):
            _ans = max(_ans , _list[i] + _list[-i -1])
        return _ans
        
        