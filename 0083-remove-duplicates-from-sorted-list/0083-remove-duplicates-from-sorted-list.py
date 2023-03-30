# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        running = head
        while running and running.next:
            if running.val == running.next.val:
                temp = running.next
                while temp and running.val == temp.val:
                    temp = temp.next
                running.next = temp
            running = running.next
        return head
