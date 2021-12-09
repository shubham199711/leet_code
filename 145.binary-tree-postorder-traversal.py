from typing import *
#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        _ans = []
        head, stack = root, []
        while len(stack) > 0 or head is not None:
            if head is None:
                head = stack.pop()
                if len(stack) > 0 and head == stack[-1]:
                    head = head.right
                else:
                    _ans.append(head.val)
                    head = None
            else:
                stack.append(head)
                stack.append(head)
                head = head.left
        return _ans
# @lc code=end

