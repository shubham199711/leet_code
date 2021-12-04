from typing import *
#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_equal(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if left and right:
            if left.val != right.val:
                return False
            if not self.is_equal(left.left, right.right) or not self.is_equal(left.right, right.left):
                return False
            return True
        return False
            
        
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.is_equal(root, root)
        
# @lc code=end

