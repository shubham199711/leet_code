# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Let large = max(p.val, q.val), small = min(p.val, q.val).
# We keep iterate root in our BST:
# If root.val > large then both node p and q belong to the left subtree, go to left by root = root.left.
# If root.val < small then both node p and q belong to the right subtree, go to right by root = root.right.
# Now, small <= root.val <= large the current root is the LCA between q and p.

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