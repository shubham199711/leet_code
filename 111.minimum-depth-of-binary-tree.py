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
    def minDepth(self, root: Optional[TreeNode],counter = 1):
        if root is None:
            return math.inf
        if root.left is None and root.right is None:
            return counter
        return min(self.minDepth(root.left, counter + 1), self.minDepth(root.right, counter + 1))
# @lc code=end

