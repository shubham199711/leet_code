# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        _max = max(p.val, q.val)
        _min = min(p.val, q.val)
        while root:
            if _max < root.val:
                root = root.left
            elif _min > root.val:
                root = root.right
            else:
                return root
        return None