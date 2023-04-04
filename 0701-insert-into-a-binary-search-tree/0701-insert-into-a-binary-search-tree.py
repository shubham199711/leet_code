# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        run = root
        while True:
            if run.val < val:
                if run.right is None:
                    run.right = TreeNode(val)
                    return root
                run = run.right
            else:
                if run.left is None:
                    run.left = TreeNode(val)
                    return root
                run = run.left
        
        