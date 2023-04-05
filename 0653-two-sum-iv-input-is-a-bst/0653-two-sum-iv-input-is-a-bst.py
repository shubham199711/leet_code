# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        cache = {}
        def bfs(head):
            if not head:
                return False
            if cache.get(head.val) is not None:
                return True
            _nextVal = k - head.val
            cache[_nextVal] = True
            return bfs(head.left) or bfs(head.right)
        
        return bfs(root)