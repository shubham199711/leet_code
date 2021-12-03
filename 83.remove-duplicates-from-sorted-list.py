from typing import *
#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = head
        prev = None
        checked = {}
        while head is not None:
            if checked.get(head.val) is not None:
                prev.next = head.next
            else:
                checked[head.val] = True
                prev = head
            head = head.next
        return root
# @lc code=end

