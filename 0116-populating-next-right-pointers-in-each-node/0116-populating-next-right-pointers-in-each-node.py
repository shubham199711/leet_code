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
        if root:
            stack = [(root, 0)]
            while len(stack) > 0:
                item, level = stack.pop(0)
                if item.left and item.right:
                    stack.append((item.left, level + 1))
                    stack.append((item.right, level + 1))
                if len(stack) and stack[0][1] == level:
                    item.next = stack[0][0]
        return root
        