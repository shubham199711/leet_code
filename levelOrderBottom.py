# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = [(root, 0)]
        _ans = []
        while queue:
            item, level = queue.pop(0)
            if level < len(_ans):
                _ans[level].append(item.val)
            else:
                _ans.insert(level,[item.val])
            if item.left is not None:
                queue.append((item.left, level + 1))
            if item.right is not None:
                queue.append((item.right, level + 1))
        return _ans[::-1]