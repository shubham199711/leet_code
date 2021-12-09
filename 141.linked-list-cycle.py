from typing import *
#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        fast_runner = head
        slow_runner = head
        while fast_runner is not None:
            if fast_runner is None:
                return False
            fast_runner = fast_runner.next
            if fast_runner is None:
                return False
            fast_runner = fast_runner.next
            if slow_runner is None:
                return False
            slow_runner = slow_runner.next
            if fast_runner == slow_runner:
                return True
        return False
# @lc code=end

