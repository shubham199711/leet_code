from typing import *
#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int , running_sum = 0) -> bool:
        if not root:
            return False
        running_sum += root.val
        if root.left is None and root.right is None and  running_sum == targetSum:
            return True
        return self.hasPathSum(root.left, targetSum, running_sum) or self.hasPathSum(root.right, targetSum, running_sum)
# @lc code=end

