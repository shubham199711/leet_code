# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        prev = None
        while temp and temp.next:
            newTemp = temp
            while newTemp and newTemp.next and newTemp.val == newTemp.next.val:
                newTemp = newTemp.next
            # print(f'{newTemp = }, {prev = } {temp = }')
            # print(prev == None and newTemp.val != temp.val)
            # print(newTemp.val != temp.val)
            if prev == None and newTemp != temp:
                head = newTemp.next
                temp = head
            elif newTemp != temp:
                prev.next = newTemp.next
                temp = newTemp.next
            else:
                prev = temp   
                temp = temp.next
        return head