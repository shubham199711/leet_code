# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):
        minVal, maxVal = float('-inf'), float('inf')
        return self.checkBST(root, minVal, maxVal)
    
    def checkBST(self, node, minVal, maxVal):
        if node is None:
            return True
        elif minVal < node.val < maxVal:
            return self.checkBST(node.left, minVal, node.val) and self.checkBST(node.right, node.val, maxVal)
        else:
            return False