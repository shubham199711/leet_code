# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        vals, q, d = [], [root], 0
        while q:
            nq, val = [], []
            for node in q:
                if node:
                    val.append(node.val)
                    nq += [node.left, node.right]
            if val: vals.append(val[::-1] if d & 1 else val)
            q, d = nq, d+1
        return vals
