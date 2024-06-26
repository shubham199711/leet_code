# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self.curr = root
        
    def next(self):
        while self.curr or self.stack:
            if self.curr:
                self.stack.append(self.curr)
                self.curr = self.curr.left
            else:
                result = self.stack.pop()
                self.curr = result.right
                return result.val
        
    def hasNext(self):
        return self.curr or self.stack

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()