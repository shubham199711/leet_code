from typing import *
#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen_dict = {}
        rootA , rootB = headA, headB
        while rootA is not None:
            seen_dict[rootA] = rootA.val
            rootA = rootA.next
        while rootB is not None:
            if seen_dict.get(rootB) is not None:
                return rootB
            rootB = rootB.next
        return None
        
# @lc code=end

