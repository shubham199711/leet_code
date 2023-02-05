# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        _sum = 0
        def dfs(head, parent, grandParent):
            nonlocal _sum
            if not head:
                return
            if grandParent is not None and grandParent % 2 == 0:
                _sum += head.val
            grandParent = parent
            parent = head.val
            dfs(head.left, parent, grandParent)
            dfs(head.right, parent, grandParent)
            
        dfs(root, None, None)
        return _sum