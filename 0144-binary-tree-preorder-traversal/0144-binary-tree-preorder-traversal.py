# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(head):
            if head is None:
                return
            ans.append(head.val)
            dfs(head.left)
            dfs(head.right)
            
        dfs(root)
        return ans
        