from typing import *
#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        newHead, knowHead = None, None
        root = head
        while root is not None:
            if root.val != val:
                if newHead is None:
                    newHead = ListNode(root.val)
                    knowHead = newHead 
                else:
                    newHead.next = ListNode(root.val) 
                    newHead = newHead.next
            root = root.next
        return knowHead
# @lc code=end

