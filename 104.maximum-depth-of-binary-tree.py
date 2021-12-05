from typing import *
#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def depth(self,root: Optional[TreeNode],depth: int) -> int:
        if not root:
            return depth - 1
        return max( depth ,self.depth(root.left, depth + 1),
        self.depth(root.right, depth + 1))
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth(root, 1)
# @lc code=end

