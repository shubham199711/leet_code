from typing import *
#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.

import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def depth(self, root: Optional[TreeNode], counter: int):
        if root is None:
            return math.inf
        if root.left is None and root.right is None:
            return counter
        return min(self.depth(root.left, counter + 1), self.depth(root.right, counter + 1))
    
    def minDepth(self, root: Optional[TreeNode]):
        if root is None:
            return 0
        return self.depth(root , 1)
# @lc code=end

