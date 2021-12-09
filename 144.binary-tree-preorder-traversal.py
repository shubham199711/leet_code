from typing import *
#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        _ans = []
        stack = []
        head = root
        while len(stack) > 0 or head is not None:
            if head is None:
                head = stack.pop()
            else:
                _ans.append(head.val)
                stack.append(head.right)
                head = head.left
        return _ans

# @lc code=end

