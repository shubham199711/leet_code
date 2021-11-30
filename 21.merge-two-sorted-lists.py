#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1 2 4
# 1 3 4
# 1(b) 1(a) 2  
class Solution:
    def mergeTwoLists(self, p, q):
        if p is None:
            return q
        head = p
        prev = None
        while p is not None:
                while q is not None and q.val <= p.val:
                    q_temp = q
                    q = q.next
                    q_temp.next = p
                    if p == head:
                        head = q_temp
                    if prev is not None:
                        prev.next = q_temp
                    prev = q_temp
                prev = p
                p = p.next
        if q is not None:
            p = head
            while p.next is not None:
                p = p.next
            p.next = q
        return head
# @lc code=end

