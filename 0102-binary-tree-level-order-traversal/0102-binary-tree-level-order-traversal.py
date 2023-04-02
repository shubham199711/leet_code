# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = [[]]
        stack = [(root, 0)]
        while len(stack):
            head, level = stack.pop(0)
            if level != len(ans) - 1:
                ans.append([])
            ans[-1].append(head.val)
            if head.left:
                stack.append((head.left, level + 1))
            if head.right:
                stack.append((head.right, level + 1))
        return ans 
        
        