from typing import *
#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        _ans = []
        stack = []
        current = root
        while len(stack) != 0 or current is not None:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                _ans.append(current.val)
                current = current.right
        return _ans
# @lc code=end

