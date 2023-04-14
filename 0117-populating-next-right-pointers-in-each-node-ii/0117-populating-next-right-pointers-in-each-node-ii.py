"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        queue = [(root, 0)]
        prev = (None, None)
        while len(queue):
            nood, level = queue.pop(0)
            prevNood, prevLevel = prev
            if prevNood != None and prevLevel == level:
                prevNood.next = nood
            prev = (nood, level)
            if nood.left is not None:
                queue.append((nood.left, level + 1))
            if nood.right is not None:
                queue.append((nood.right, level + 1))
        return root
            
            
            
        
        